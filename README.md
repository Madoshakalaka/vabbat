# vabbat

[![Build Status](https://travis-ci.org/Madoshakalaka/vabbat.svg)](https://travis-ci.org/Madoshakalaka/vabbat)
[![codecov](https://codecov.io/gh/Madoshakalaka/vabbat/branch/master/graph/badge.svg)](https://codecov.io/gh/Madoshakalaka/vabbat)
[![PyPI version](https://badge.fury.io/py/vabbat.svg)](https://badge.fury.io/py/vabbat)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/vabbat.svg)](https://pypi.python.org/pypi/vabbat/)


## Installation

`pip install vabbat`

## What Does It Do

<!--You picture won't show on pypi if you use relative path.-->
<!--If you want to add any image, please add the image to readme_assets folder and add the filename as below-->
<!--![some show case picture](https://raw.githubusercontent.com/Madoshakalaka/vabbat/master/readme_assets/showcasePicture.png)-->

Traffic video compression using background subtraction and bounding box matching.

See this amazing [youtube video demo](https://youtu.be/Uqwgp-7tqpA?t=181)

![steps](https://raw.githubusercontent.com/Madoshakalaka/vabbat/master/readme_assets/steps.png)

![result](https://raw.githubusercontent.com/Madoshakalaka/vabbat/master/readme_assets/result.png)





## How to Use

Pip creates command line executable entry point by default

You should be able to run shell command `$ vabbat` anywhere.

For a demonstration, you can download [this test video](https://github.com/Madoshakalaka/vabbat/blob/master/tests/data/trafficVideo.mp4?raw=true) and run:

- `$ vabbat trafficVideo.mp4` which produces `compressed_video.mp4` under current directory

- `$ vabbat trafficVideo.mp4 --mode demo` which presents an interactive demonstration

- `$ vabbat -h` for more help

in case the command does not work (e.g. on windows when <python_dir>/Scripts is not in system path). Use the package entry:

`> python -m vabbat`

## Limitations

- The camera should be stationary
- The video should be a top down view without cars blocking line of sight from other cars.
