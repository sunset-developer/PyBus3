[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">PyBus3</h3>

  <p align="center">
    A simple and efficient eventbus for python 3.6+ 
    <br />
    <a href="https://github.com/sunset-developer/PyBus3/issues">Report Bug</a>
    ·
    <a href="https://github.com/sunset-developer/PyBus3/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

PyBus3 is an event bus library inspired by Guava's library. Using the publisher/subscriber pattern for loose coupling, EventBus enables central communication to decoupled classes with just a few lines of code. This simplifies the code, removes dependencies, and speeds up app development.

Your benefits using EventBus: It… 
* Simplifies the communication between components.
* Uses async/await syntax.
* Avoids complex and error-prone dependencies and life cycle issues.
* Is fast; specifically optimized for high performance.
* Is tiny.

<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

You need pip in order to install PyBus3.
* pip
```sh
sudo apt-get install python3-pip
```

### Installation

Clone the repo, or install using pip.
```sh
pip install PyBus3
```

<!-- USAGE EXAMPLES -->
## Usage
1: Define events.
```
class TestEvent:
    def __init__(self, message):
        self.message = message
```

2: Register your subscriber.
```
class TestClass:
    def __init__(self):
        bus.register(self)
        self.test_message = None
```

3: Prepare subscribers.
```
@subscribe(TestEvent)
async def onTestEvent(self, event):
    self.test_message = event.message
```

4: Post events.
```
test_class = TestClass()
await bus.post(TestEvent('test message'))
self.assertEqual(test_class.test_message, 'test message')
```


<!-- ROADMAP -->
## Roadmap

Currently PyBus3 only has capabilties with async/await syntax. 

Future versions will include non async thread delivery. 

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Email: aidanstewart@sunsetdeveloper.com

Project Link: [https://github.com/sunset-developer/PyBus3](https://github.com/sunset-developer/PyBus3)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Be the first! Submit a pull request.](https://github.com/sunset-developer/PyBus3/pulls)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/sunset-developer/PyBus3.svg?style=flat-square
[contributors-url]: https://github.com/sunset-developer/PyBus3/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sunset-developer/PyBus3.svg?style=flat-square
[forks-url]: https://github.com/sunset-developer/PyBus3/network/members
[stars-shield]: https://img.shields.io/github/stars/sunset-developer/PyBus3.svg?style=flat-square
[stars-url]: https://github.com/sunset-developer/PyBus3/stargazers
[issues-shield]: https://img.shields.io/github/issues/sunset-developer/PyBus3.svg?style=flat-square
[issues-url]: https://github.com/sunset-developer/PyBus3/issues
[license-shield]: https://img.shields.io/github/license/sunset-developer/PyBus3.svg?style=flat-square
[license-url]: https://github.com/sunset-developer/PyBus3/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
