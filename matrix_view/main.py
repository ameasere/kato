from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from aeskeyschedule import key_schedule
import json
import sys
import traceback
from ui_main import Ui_MainWindow


# https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/
class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    '''
    finished = Signal()  # QtCore.Signal
    error = Signal(tuple)
    result = Signal(object)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()  # QtCore.Slot
    def run(self):
        """
        Initialise the runner function with passed args, kwargs.
        """

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            trackback_str = traceback.format_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, trackback_str))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.method = None
        self.k = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dragPos = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        self.first_placeholder_row = [self.ui.placeholder_1, self.ui.placeholder_4, self.ui.placeholder_7,
                                      self.ui.placeholder_10, self.ui.placeholder_13, self.ui.placeholder_16]
        self.second_placeholder_row = [self.ui.placeholder_2, self.ui.placeholder_5, self.ui.placeholder_8,
                                       self.ui.placeholder_11, self.ui.placeholder_14, self.ui.placeholder_17]
        self.third_placeholder_row = [self.ui.placeholder_3, self.ui.placeholder_6, self.ui.placeholder_9,
                                      self.ui.placeholder_12, self.ui.placeholder_15, self.ui.placeholder_18]
        self.final_placeholder_column = [self.ui.placeholder_16, self.ui.placeholder_17, self.ui.placeholder_18]

        self.initial_matrix_labels = [self.ui.matrix00, self.ui.matrix01, self.ui.matrix02, self.ui.matrix03,
                                      self.ui.matrix04]
        self.second_row_labels = [self.ui.matrix10, self.ui.matrix11, self.ui.matrix12, self.ui.matrix13,
                                  self.ui.matrix14]
        self.third_row_labels = [self.ui.matrix20, self.ui.matrix21, self.ui.matrix22, self.ui.matrix23,
                                 self.ui.matrix24]
        self.fourth_row_labels = [self.ui.matrix30, self.ui.matrix31, self.ui.matrix32, self.ui.matrix33,
                                  self.ui.matrix34]
        self.final_column_labels = [self.ui.matrix_final_00, self.ui.matrix_final_10, self.ui.matrix_final_20,
                                    self.ui.matrix_final_30]

        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

        # Any dragging on the window will move it
        self.ui.dragBar.mouseMoveEvent = moveWindow

        self.ui.btn_close.clicked.connect(self.close)

        self.ui.encrypt_button.clicked.connect(self.encrypt_callback)
        self.ui.decrypt_button.clicked.connect(self.decrypt_callback)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

    def fill_matrices(self, final_state):
        self.ui.status_label.setText("")
        self.k._Kato__initial_state_matrix = self.k._Kato__initial_state_matrix[
                                             :5] + self.k._Kato__initial_state_matrix[-1:]
        self.k._Kato__e_post_substitution = self.k._Kato__e_post_substitution[:5] + self.k._Kato__e_post_substitution[
                                                                                    -1:]
        self.k._Kato__e_post_transposition = self.k._Kato__e_post_transposition[
                                             :5] + self.k._Kato__e_post_transposition[-1:]
        self.k._Kato__e_post_key_addition = self.k._Kato__e_post_key_addition[:5] + self.k._Kato__e_post_key_addition[
                                                                                    -1:]
        self.k._Kato__d_post_key_addition = self.k._Kato__d_post_key_addition[:5] + self.k._Kato__d_post_key_addition[
                                                                                    -1:]
        self.k._Kato__d_post_transposition = self.k._Kato__d_post_transposition[
                                             :5] + self.k._Kato__d_post_transposition[-1:]
        self.k._Kato__d_post_substitution = self.k._Kato__d_post_substitution[:5] + self.k._Kato__d_post_substitution[
                                                                                    -1:]

        if self.method == "encrypt":
            # Fill initial matrices.
            # Set text for initial matrices to a formatted version of the 2D array
            count = 0
            for i in self.k._Kato__initial_state_matrix:
                # If it is the last element, skip
                if count >= 5:
                    break
                # Remove first and last character
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.initial_matrix_labels[count].setText(i)
                count += 1

            # First placeholder row should be filled with text: "Post Substitution"
            for i in self.first_placeholder_row:
                i.setText("Post Substitution")

            count = 0
            for i in self.k._Kato__e_post_substitution:
                if count >= 5:
                    break
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.second_row_labels[count].setText(i)
                count += 1

            for i in self.second_placeholder_row:
                i.setText("Post Transposition")

            count = 0
            for i in self.k._Kato__e_post_transposition:
                if count >= 5:
                    break
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.third_row_labels[count].setText(i)
                count += 1

            for i in self.third_placeholder_row:
                i.setText("Post Key Addition")

            count = 0
            for i in self.k._Kato__e_post_key_addition:
                if count >= 5:
                    break
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.fourth_row_labels[count].setText(i)
                count += 1

            # Final column elements are the last element in each Kato array
            final_column = [self.k._Kato__initial_state_matrix[-1], self.k._Kato__e_post_substitution[-1],
                            self.k._Kato__e_post_transposition[-1], self.k._Kato__e_post_key_addition[-1]]
            count = 0
            for i in final_column:
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.final_column_labels[count].setText(i)
                count += 1

            self.ui.ciphertext_field.setText(str(final_state))
            print(type(final_state))
        elif self.method == "decrypt":
            # Fill initial matrices.
            # Set text for initial matrices to a formatted version of the 2D array
            count = 0
            for i in self.k._Kato__initial_state_matrix:
                # If it is the last element, skip
                if count >= 5:
                    break
                # Remove first and last character
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.initial_matrix_labels[count].setText(i)
                count += 1

            # First placeholder row should be filled with text: "Post Key Addition"
            for i in self.first_placeholder_row:
                i.setText("Post Key Addition")

            count = 0
            for i in self.k._Kato__d_post_key_addition:
                if count >= 5:
                    break
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.second_row_labels[count].setText(i)
                count += 1

            for i in self.second_placeholder_row:
                i.setText("Post Transposition")

            count = 0
            for i in self.k._Kato__d_post_transposition:
                if count >= 5:
                    break
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.third_row_labels[count].setText(i)
                count += 1

            for i in self.third_placeholder_row:
                i.setText("Post Substitution")

            count = 0
            for i in self.k._Kato__d_post_substitution:
                if count >= 5:
                    break
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.fourth_row_labels[count].setText(i)
                count += 1

            # Final column elements are the last element in each Kato array
            final_column = [self.k._Kato__initial_state_matrix[-1], self.k._Kato__d_post_key_addition[-1],
                            self.k._Kato__d_post_transposition[-1], self.k._Kato__d_post_substitution[-1]]
            count = 0
            for i in final_column:
                i = str(i)[1:-1]
                i = i.replace("], ", "\n")
                i = i.replace("[", "")
                i = i.replace("]", "")
                self.final_column_labels[count].setText(i)
                count += 1

            if type(final_state) == list:
                self.ui.plaintext_field.setText(str(final_state))
            else:
                try:
                    self.ui.plaintext_field.setText(final_state.decode("utf-8"))
                except Exception as e:
                    if len(str(final_state)) > 16:
                        self.ui.plaintext_field.setText(str(final_state)[:10] + "...")
                    else:
                        self.ui.plaintext_field.setText(str(final_state))

    def encrypt_callback(self):
        key = self.ui.key_field.text()
        plaintext = self.ui.plaintext_field.text()
        iv = self.ui.iv_field.text()
        if len(key) != 16:
            self.ui.status_label.setText("Key must be 16 bytes long.")
            return
        if len(plaintext) != 16:
            self.ui.status_label.setText("Plaintext must be 16 bytes long.")
            return
        if iv and len(iv) != 16:
            self.ui.status_label.setText("IV must be 16 bytes long.")
            return

        try:
            key = bytes(key, "utf-8")
            plaintext = bytes(plaintext, "utf-8")
            iv = bytes(iv, "utf-8") if iv else None

            self.k = Kato(key, iv)
            self.method = "encrypt"
            worker = Worker(self.k.encrypt, plaintext)
            worker.signals.result.connect(self.fill_matrices)
            QThreadPool.globalInstance().start(worker)
        except Exception as e:
            print(e)
            self.ui.status_label.setText("Invalid key, plaintext, or IV.")
            return

    def decrypt_callback(self):
        key = self.ui.key_field.text()
        ciphertext = self.ui.ciphertext_field.text()
        iv = self.ui.iv_field.text()
        if len(key) != 16:
            self.ui.status_label.setText("Key must be 16 bytes long.")
            return
        if iv and len(iv) != 16:
            self.ui.status_label.setText("IV must be 16 bytes long.")
            return
        # Ciphertext should be a list of lists.
        # List of 4 arrays, each having 4 numbers.
        # If not, error.
        try:
            key = bytes(key, "utf-8")
            iv = bytes(iv, "utf-8") if iv else None
            ciphertext = json.loads(ciphertext)
            self.k = Kato(key, iv)
            self.method = "decrypt"
            worker = Worker(self.k.decrypt, ciphertext)
            worker.signals.result.connect(self.fill_matrices)
            worker.signals.error.connect(lambda x: print(x[1]))
            QThreadPool.globalInstance().start(worker)
        except Exception as e:
            print(e)
            self.ui.status_label.setText("Invalid key, ciphertext, or IV.")
            return


class Kato:
    def __init__(self, key, iv=None):

        self.__plaintext = None
        self.__ciphertext = None
        self.__key = None

        self.__initial_state_matrix = []
        self.__e_post_substitution = []
        self.__e_post_transposition = []
        self.__e_post_key_addition = []

        self.__d_post_key_addition = []
        self.__d_post_transposition = []
        self.__d_post_substitution = []

        if iv is not None:
            if not isinstance(iv, bytes):
                raise KatoInternalError("IV must be a bytes-like object, 461")
            elif not len(iv) == 16:
                raise KatoInternalError("IV must be 16 bytes long, 462")
            else:
                self.__iv = iv
        else:
            self.__iv = None

        if not isinstance(key, bytes):
            raise KatoInternalError("Key must be a bytes-like object, 461")

        elif not len(key) == 16:
            raise KatoInternalError("Key must be 16 bytes long, 462")
        else:
            self.__key = key

        self.key_length = len(key)
        self.s_box = [  # Implemented custom S-Box from paper: doi: 10.1016/j.protcy.2013.12.443
            [0x31, 0x2E, 0x04, 0xAB, 0xC6, 0x70, 0x91, 0x61, 0x19, 0x9F, 0xDC, 0x7D, 0xAD, 0x7F, 0xAC, 0xFF],
            [0x56, 0x82, 0xE8, 0x67, 0xA0, 0x43, 0xB2, 0x4A, 0x36, 0x08, 0x17, 0x22, 0xB8, 0x4F, 0x0E, 0xAE],
            [0xFE, 0xD6, 0x78, 0x95, 0xD9, 0x45, 0x0B, 0x96, 0x58, 0x3F, 0x8C, 0x55, 0x03, 0x92, 0xE0, 0x63],
            [0x18, 0x1F, 0x26, 0x00, 0x13, 0x9A, 0xE4, 0xDB, 0x44, 0x8B, 0x6C, 0x25, 0x81, 0x69, 0x1D, 0x27],
            [0x80, 0xE9, 0xE7, 0x5A, 0x3E, 0x0C, 0xAF, 0x7E, 0x2C, 0x05, 0x2B, 0x3C, 0x0D, 0x2F, 0x84, 0x51],
            [0xBB, 0xCE, 0x74, 0x29, 0x3D, 0x8D, 0xD5, 0xF9, 0xEF, 0x5E, 0x86, 0x50, 0x3B, 0x34, 0x09, 0x97],
            [0xD8, 0xC5, 0xF1, 0xEB, 0xE6, 0xDA, 0xC4, 0x71, 0x11, 0x9B, 0x64, 0x21, 0x39, 0x35, 0x89, 0x6D],
            [0xA5, 0x7B, 0x14, 0xA3, 0xC2, 0xC8, 0xCD, 0xF5, 0x53, 0xBA, 0x4E, 0x8E, 0x54, 0x83, 0x68, 0x9D],
            [0xDD, 0xFD, 0x57, 0x02, 0x12, 0x1A, 0x1E, 0xA6, 0xFA, 0x6E, 0x24, 0x01, 0x93, 0x60, 0x99, 0x65],
            [0xA1, 0xC3, 0x48, 0x37, 0x88, 0xED, 0x5F, 0x06, 0xAA, 0x46, 0x8A, 0xEC, 0xDF, 0xFC, 0xD7, 0xF8],
            [0x6F, 0xA4, 0xFB, 0xEE, 0xDE, 0x7C, 0x2D, 0x85, 0xD1, 0x41, 0xB3, 0xCA, 0xCC, 0x75, 0xA9, 0xC7],
            [0xF0, 0x6B, 0x1C, 0xA7, 0x7A, 0x94, 0x59, 0xBF, 0x76, 0x28, 0xBD, 0x77, 0xA8, 0x47, 0x0A, 0x16],
            [0xA2, 0x42, 0x32, 0xB0, 0x4B, 0xB6, 0xF2, 0x6A, 0x9C, 0x5D, 0x07, 0x2A, 0xBC, 0xF7, 0x52, 0x3A],
            [0xB4, 0xF3, 0xEA, 0x66, 0x20, 0xB9, 0xCF, 0xF4, 0xD3, 0x40, 0x33, 0x30, 0xB1, 0xCB, 0x4C, 0x8F],
            [0xD4, 0x79, 0x15, 0x23, 0x38, 0xB5, 0x73, 0x10, 0x1B, 0x9E, 0x5C, 0x87, 0xD0, 0xC1, 0x49, 0xB7],
            [0x72, 0x90, 0xE1, 0xE3, 0xE2, 0x62, 0x98, 0xE5, 0x5B, 0xBE, 0xF6, 0xD2, 0xC0, 0xC9, 0x4D, 0x0F]
        ]

        self.inv_s_box = [
            # Implemented custom inverse S-Box from above S-Box.
            [0x33, 0x8B, 0x83, 0x2C, 0x02, 0x49, 0x97, 0xCA, 0x19, 0x5E, 0xBE, 0x26, 0x45, 0x4C, 0x1E, 0xFF],
            [0xE7, 0x68, 0x84, 0x34, 0x72, 0xE2, 0xBF, 0x1A, 0x30, 0x08, 0x85, 0xE8, 0xB2, 0x3E, 0x86, 0x31],
            [0xD4, 0x6B, 0x1B, 0xE3, 0x8A, 0x3B, 0x32, 0x3F, 0xB9, 0x53, 0xCB, 0x4A, 0x48, 0xA6, 0x01, 0x4D],
            [0xDB, 0x00, 0xC2, 0xDA, 0x5D, 0x6D, 0x18, 0x93, 0xE4, 0x6C, 0xCF, 0x5C, 0x4B, 0x54, 0x44, 0x29],
            [0xD9, 0xA9, 0xC1, 0x15, 0x38, 0x25, 0x99, 0xBD, 0x92, 0xEE, 0x17, 0xC4, 0xDE, 0xFE, 0x7A, 0x1D],
            [0x5B, 0x4F, 0xCE, 0x78, 0x7C, 0x2B, 0x10, 0x82, 0x28, 0xB6, 0x43, 0xF8, 0xEA, 0xC9, 0x59, 0x96],
            [0x8D, 0x07, 0xF5, 0x2F, 0x6A, 0x8F, 0xD3, 0x13, 0x7E, 0x3D, 0xC7, 0xB1, 0x3A, 0x6F, 0x89, 0xA0],
            [0x05, 0x67, 0xF0, 0xE6, 0x52, 0xAD, 0xB8, 0xBB, 0x22, 0xE1, 0xB4, 0x71, 0xA5, 0x0B, 0x47, 0x0D],
            [0x40, 0x3C, 0x11, 0x7D, 0x4E, 0xA7, 0x5A, 0xEB, 0x94, 0x6E, 0x9A, 0x39, 0x2A, 0x55, 0x7B, 0xDF],
            [0xF1, 0x06, 0x2D, 0x8C, 0xB5, 0x23, 0x27, 0x5F, 0xF6, 0x8E, 0x35, 0x69, 0xC8, 0x7F, 0xE9, 0x09],
            [0x14, 0x90, 0xC0, 0x73, 0xA1, 0x70, 0x87, 0xB3, 0xBC, 0xAE, 0x98, 0x03, 0x0E, 0x0C, 0x1F, 0x46],
            [0xC3, 0xDC, 0x16, 0xAA, 0xD0, 0xE5, 0xC5, 0xEF, 0x1C, 0xD5, 0x79, 0x50, 0xCC, 0xBA, 0xF9, 0xB7],
            [0xFC, 0xED, 0x74, 0x91, 0x66, 0x61, 0x04, 0xAF, 0x75, 0xFD, 0xAB, 0xDD, 0xAC, 0x76, 0x51, 0xD6],
            [0xEC, 0xA8, 0xFB, 0xD8, 0xE0, 0x56, 0x21, 0x9E, 0x60, 0x24, 0x65, 0x37, 0x0A, 0x80, 0xA4, 0x9C],
            [0x2E, 0xF2, 0xF4, 0xF3, 0x36, 0xF7, 0x64, 0x42, 0x12, 0x41, 0xD2, 0x63, 0x9B, 0x95, 0xA3, 0x58],
            [0xB0, 0x62, 0xC6, 0xD1, 0xD7, 0x77, 0xFA, 0xCD, 0x9F, 0x57, 0x88, 0xA2, 0x9D, 0x81, 0x20, 0x0F]
        ]

        self.rounds = 10

    @staticmethod
    def transpose_matrix(matrix):
        n = len(matrix)

        # Transpose the matrix
        transposed = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                transposed[i][j] = matrix[j][i]

        return transposed

    @staticmethod
    def __add_round_key(state, round_key):
        """
        Performs the AddRoundKey operation in Rijndael/AES encryption.

        Parameters:
        state (list of lists): The state matrix (4x4) representing the current state.
        round_key (bytes): The round key to be added to the state matrix.

        Returns:
        list of lists: The resulting state matrix after adding the round key.
        """
        # Convert round_key from bytes to a 4x4 matrix
        round_key = [[round_key[i + 4 * j] for i in range(4)] for j in range(4)]
        result_state = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result_state[i][j] = state[i][j] ^ round_key[i][j]
        return result_state

    @staticmethod
    def omflip_matrix(input_matrix, key):
        # Constants for bitwise operations
        mask = 0xFFFFFFFF
        shift = 5

        # Perform linear permutation
        output_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j, pos in enumerate(key):
                output_matrix[i][j] = input_matrix[i][pos]

        # Perform bitwise operations
        for i in range(4):
            for j in range(4):
                output_matrix[i][j] = ((output_matrix[i][j] << shift) | (output_matrix[i][j] >> (32 - shift))) & mask

        return output_matrix

    @staticmethod
    def omflip_decrypt_matrix(encrypted_matrix, key):
        # Constants for bitwise operations
        mask = 0xFFFFFFFF
        shift = 5

        # Inverse permutation of the key
        inv_key = [key.index(i) for i in range(4)]

        # Reverse bitwise operations
        decrypted_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                decrypted_matrix[i][j] = ((encrypted_matrix[i][j] >> shift) | (
                        encrypted_matrix[i][j] << (32 - shift))) & mask

        # Reverse linear permutation
        output_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j, pos in enumerate(inv_key):
                output_matrix[i][j] = decrypted_matrix[i][pos]

        return output_matrix

    @staticmethod
    def cipher_block_chaining(block, iv):
        """
        Performs the CBC operation on a block of ciphertext.

        Parameters:
        block (bytes): The block of ciphertext to be processed.
        iv (bytes): The initialization vector to be used.

        Returns:
        bytes: The resulting block of ciphertext after CBC.
        """
        # XOR the block with the IV
        # The block is a 4x4 matrix, list of lists
        result_block = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result_block[i][j] = block[i][j] ^ iv[i * 4 + j]
        return result_block

    def encrypt(self, plaintext):
        """
        if not isinstance(plaintext, bytes):
            raise KatoInternalError("Plaintext must be a bytes-like object, 461")
        else:
            self.__plaintext = plaintext  # Private attribute.
        """

        # 1: Key Expansion
        # 2: Initial Round
        # 3: Rounds

        # Initial State with plaintext
        state = []
        for i in range(0, len(plaintext), 4):
            state.append([plaintext[i], plaintext[i + 1], plaintext[i + 2], plaintext[i + 3]])
        # Key Expansion
        round_keys = key_schedule(self.__key)
        # XOR this with the initial key
        try:
            for n in range(self.rounds):
                if self.__iv is not None:
                    state = self.cipher_block_chaining(state, self.__iv)
                self.__initial_state_matrix.append(state)
                state = [[self.s_box[state[i][j] // 16][state[i][j] % 16] for j in range(4)] for i in range(4)]
                self.__e_post_substitution.append(state)
                state = self.transpose_matrix(state)
                self.__e_post_transposition.append(state)
                state = self.__add_round_key(state, round_keys[n + 1])
                self.__e_post_key_addition.append(state)
            state = self.omflip_matrix(state, [3, 1, 0, 2])
        except Exception:
            raise KatoInternalError(f"An error occurred during encryption, likely incorrect key/IV pair or plaintext.")

        # TEMP: convert to ciphertext bytes
        # Return as list of lists
        # We can't return as bytes, as all the hex numbers are >1000
        return state

    def decrypt(self, ciphertext):
        """
        if not isinstance(ciphertext, bytes):
            raise KatoInternalError("Ciphertext must be a bytes-like object, 461")
        else:
            self.__ciphertext = ciphertext  # Private attribute.
        """

        # Decryption: do everything in reverse order.

        # 1. Make the state matrix from the ciphertext
        # Reverse of b"".join([bytes(row) for row in state])
        state = ciphertext

        # 2. Initial Round Key Expansion (in reverse)
        round_keys = key_schedule(self.__key)[::-1]
        try:
            state = self.omflip_decrypt_matrix(state, [3, 1, 0, 2])
            for n in range(self.rounds):
                self.__initial_state_matrix.append(state)
                state = self.__add_round_key(state, round_keys[n])
                self.__d_post_key_addition.append(state)
                state = self.transpose_matrix(state)
                self.__d_post_transposition.append(state)
                state = [[self.inv_s_box[state[i][j] // 16][state[i][j] % 16] for j in range(4)] for i in range(4)]
                self.__d_post_substitution.append(state)
                if self.__iv is not None:
                    state = self.cipher_block_chaining(state, self.__iv)
            # If any digit in the state matrix is > 255, it will raise an error, so return the state matrix.
            if any(any(i > 255 for i in row) for row in state):
                return state
            else:
                return b"".join(bytes(row) for row in state)
        except Exception:
            raise KatoInternalError(f"An error occurred during decryption, likely incorrect key/IV pair or ciphertext.")


# /// Exception Handlers ///

class KatoInternalError(Exception):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        self.with_traceback(None)  # Tracebacks can leak sensitive information.

        super().__init__(message)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.message}, {self.code}"

    def __str__(self):
        return self.message


class KatoInternalWarning(Warning):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        self.with_traceback(None)  # Tracebacks can leak sensitive information.

        super().__init__(message)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.message}, {self.code}"

    def __str__(self):
        return self.message


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
