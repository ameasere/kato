<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ameasere/kato">
    <img src="https://i.imgur.com/N9lglLk.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Kato (NetCloud24)</h3>

  <p align="center">
    A Rijndael-inspired cryptographic proof-of-concept algorithm.
    <br />
    <br />
    <a href="https://github.com/ameasere/kato">View Demo</a>
    ·
    <a href="https://github.com/ameasere/kato/issues">Report Bug</a>
    ·
    <a href="https://github.com/ameasere/kato/issues">Request Feature</a>
  </p>
</div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL3 License][license-shield]][license-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fameasere%2Fkato.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fameasere%2Fkato?ref=badge_large)

## About The Project

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fameasere%2Fkato.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fameasere%2Fkato?ref=badge_shield)

Kato is a cryptographic proof-of-concept algorithm inspired by AES (Rijndael), or the Advanced Encryption Standard. As a symbol of power, Kato serves as a hybridization focusing on efficiency and versatility without compromising security. We welcome **any** and **all** contributions towards the implementation and empowerment of the algorithm, aiming to become more than just a conceptualized technology.

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is a minimal example of getting Kato operating locally. You may require additional steps, modification or a customized implementation to suit your needs.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
  * Ensure you also have **pip** installed.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```

   **OR**

   Install using **pip** from the Python Package Index (PyPI)
   ```sh
    pip install kato
    ```
2. Import into your script
    ```python
    from kato import Kato
    ```

<p align="right">(<a href="#readme-top">Back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Below are the minimal usage examples, as well as the returned types from Kato.

<details><summary>Encrypting</summary>

**ECB** Mode:

```python
from kato import Kato

key = bytes(random.sample(range(256), 16))
k = Kato(key)
ciphertext = k.encrypt(bytes("abcdefghijklmnop","utf-8"))
```

**CBC** Mode:

```python
from kato import Kato

key = bytes(random.sample(range(256), 16))
iv = bytes(random.sample(range(256), 16))
k = Kato(key, iv)
ciphertext = k.encrypt(bytes("abcdefghijklmnop","utf-8"))
```

</details>

<details><summary>Decrypting</summary>

```python
plaintext = k.decrypt(ciphertext)
```

</details>


Each Kato class instance will have a key (and optionally, an Initialization Vector) as an attribute. This means you will have to create new Kato instances for each key (and IV pair) you wish to use.

<details><summary>Types</summary>

* **Kato.__init__()**:
    * **key**: 16 bytes
    * **iv** (Optional): 16 bytes

* **Kato.encrypt()**: Returns a 2D Array (list of lists)
    * **plaintext**: 16 bytes
    * **Example Return**: `[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`

* **Kato.decrypt()**: Returns a bytes object or 2D Array (list of lists)
    * **ciphertext**: 16 bytes
    * **Example Return**: `b'abcdefghijklmnop'` or `[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`
      * **Note**: If any digit in the state matrix cannot be decoded into hex bytes, the function will return a 2D Array.

* **Kato.cipher_block_chaining()**: Returns a bytes object.
    * **block**: 16 bytes
    * **IV** (Optional): 16 bytes
    * **Example Return**: `b'\xxx\xxx\xxx\xxx'`
      * **Note**: This CBC implementation is NOT true CBC, instead a mock-CBC simplying XORing the IV with the block before encryption and after decryption.

* **Kato.transpose_matrix()**: Returns a 2D Array (list of lists)
    * **matrix**: 4x4 2D Array
    * **Example Return**: `[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`

* **Kato.omflip_matrix()**: Returns a 2D Array (list of lists)
    * **matrix**: 4x4 2D Array
    * **key**: Array of 4 digits (default is `[3, 1, 0, 2]`)
    * **Example Return**: `[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`

* **Kato.omflip_decrypt_matrix()**: Returns a 2D Array (list of lists)
    * **matrix**: 4x4 2D Array
    * **key**: Array of 4 digits (default is `[3, 1, 0, 2]`)
    * **Example Return**: `[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`

* **Kato.__add_round_key()**: Returns a 2D Array (list of lists)
    * **state**: 4x4 2D Array
    * **round_key**: 16 bytes
    * **Example Return**: `[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]`

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add true CBC mode.
- [ ] C implementation.

See the [open issues](https://github.com/ameasere/kato/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- CREDITS -->
## Credits

Leighton Brooks - [leigh@ameasere.com](mailto:leigh@ameasere.com)  
Milena Bosiacka - [social](link)  
Riza Demirbas - [social](link)  
Sam Truss - [social](link)  
Yuliia Yavorska  - [social](link)  

Project Link: [https://github.com/ameasere/kato](https://github.com/ameasere/kato)

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ameasere/kato.svg?style=for-the-badge
[contributors-url]: https://github.com/ameasere/kato/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ameasere/kato.svg?style=for-the-badge
[forks-url]: https://github.com/ameasere/kato/network/members
[stars-shield]: https://img.shields.io/github/stars/ameasere/kato.svg?style=for-the-badge
[stars-url]: https://github.com/ameasere/kato/stargazers
[issues-shield]: https://img.shields.io/github/issues/ameasere/kato.svg?style=for-the-badge
[issues-url]: https://github.com/ameasere/kato/issues
[license-shield]: https://img.shields.io/github/license/ameasere/kato.svg?style=for-the-badge
[license-url]: https://github.com/ameasere/kato/blob/master/LICENSE.txt
[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Python-url]: https://python.org/