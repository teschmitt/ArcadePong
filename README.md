# ArcadePong

Implementation of the game classic Pong using Paul V Craven's Arcade Library. It started out just as a short test of the library's scope and ended up as a very fun and educational side project that actually taught me a lot.

## Getting Started

Grab a copy of `virtualenv` or `virtualenvwrapper` and set up a virtual environment with the Python 3.6 interpreter (see [Prerequisites](#prerequisites)) to separate the dependencies for this project. Then it's the same old same old:

```
git clone https://github.com/mrgnth/ArcadePong.git
pip install -r requirements
```

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

ArcadePong uses the wonderful [Arcade Library](https://github.com/pvcraven/arcade) for Python, which in turn depends on Python 3.6. Running `pip freeze` should give you something like this:

* arcade==1.3.0
* future==0.16.0
* Pillow==5.0.0
* pyglet==1.3.1

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Paul V Craven for all the work on his fun Arcade Library
* The original creator of Pong, [Allan Alcorn](https://en.wikipedia.org/wiki/Allan_Alcorn)
* Four Tet for the soundtrack of my coding experience
