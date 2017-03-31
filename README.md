# Moving Starfield

It works better in Python3 for some reason, so that is required.

- Run `./setup.sh` to install Python dependencies.
- Run `./starfield.py` to run.

## A moderately interesting fact about how this works

For any star, you measure the distance between the centre of the screen and it. Then you multiply that by some imaginary *z*-dimension. Then divide that by 100 so that it is a reasonable number. This allows you to derive the illusion of distance.

For example, suppose star *x* is 700 pixels from the left-hand side and the centre is 500 pixels from the left. Then the difference between the two is 200. Then that is multiplied by the *z*-dimension, for example the number 2, to make 400 - which is then divided by 100 to get 4. So the rate of change is 4 pixels. But now *x* is 204 pixels from the centre. Thus we have: 204 * 2 = 408. 408 / 100 = 4.8. So now the rate of change is 4.8 pixels, which was greater than the first rate of change. Thus the stars will appear to move faster as they move further from the centre, creating the illusion of distance to the viewer.
