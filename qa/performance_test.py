import timeit
import random
import kato
import colorama

key = bytes(random.sample(range(256), 16))
iv = bytes(random.sample(range(256), 16))
data_1 = bytes(random.choices(range(256), k=1024))
data_2 = bytes(random.choices(range(256), k=2048))
data_3 = bytes(random.choices(range(256), k=4096))

ciphertext_array = []


def test_kato_cbc():
    k = kato.Kato(key, iv)
    # Encrypt in 16-byte blocks
    start = timeit.default_timer()
    for i in range(0, len(data_1), 16):
        state = k.encrypt(data_1[i:i + 16])
        ciphertext_array.append(state)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato e-CBC 1024 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")
    start = timeit.default_timer()
    for i in ciphertext_array:
        k.decrypt(i)
        ciphertext_array.remove(i)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato d-CBC 1024 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")

    start = timeit.default_timer()
    for i in range(0, len(data_2), 16):
        state = k.encrypt(data_2[i:i + 16])
        ciphertext_array.append(state)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato e-CBC 2048 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")
    start = timeit.default_timer()
    for i in ciphertext_array:
        k.decrypt(i)
        ciphertext_array.remove(i)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato d-CBC 2048 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")

    start = timeit.default_timer()
    for i in range(0, len(data_3), 16):
        state = k.encrypt(data_3[i:i + 16])
        ciphertext_array.append(state)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato e-CBC 4096 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")
    start = timeit.default_timer()
    for i in ciphertext_array:
        k.decrypt(i)
        ciphertext_array.remove(i)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato d-CBC 4096 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")


def test_kato_ecb():
    k = kato.Kato(key)
    # Encrypt in 16-byte blocks
    start = timeit.default_timer()
    for i in range(0, len(data_1), 16):
        state = k.encrypt(data_1[i:i + 16])
        ciphertext_array.append(state)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato e-ECB 1024 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")
    start = timeit.default_timer()
    for i in ciphertext_array:
        k.decrypt(i)
        ciphertext_array.remove(i)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato d-ECB 1024 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")

    start = timeit.default_timer()
    for i in range(0, len(data_2), 16):
        state = k.encrypt(data_2[i:i + 16])
        ciphertext_array.append(state)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato e-ECB 2048 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")
    start = timeit.default_timer()
    for i in ciphertext_array:
        k.decrypt(i)
        ciphertext_array.remove(i)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato d-ECB 2048 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")

    start = timeit.default_timer()
    for i in range(0, len(data_3), 16):
        state = k.encrypt(data_3[i:i + 16])
        ciphertext_array.append(state)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato e-ECB 4096 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")
    start = timeit.default_timer()
    for i in ciphertext_array:
        k.decrypt(i)
        ciphertext_array.remove(i)
    end = timeit.default_timer()
    print(f"{colorama.Fore.GREEN}Kato d-ECB 4096 bytes: {colorama.Fore.BLUE}{round(end - start, 2)} seconds.{colorama.Fore.RESET}")


if __name__ == "__main__":
    test_kato_cbc()
    test_kato_ecb()
