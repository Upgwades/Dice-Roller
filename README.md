# Dice-Roller

This project was created to serve as the backbone to a Discord powered dice roller for use in games like D&D.

Made to be used by players who are flakey, inconsistent, and generally should not be trusted with money; the simple script accepts a variety of erratic inputs for dice rolls. The following are all 100% acceptable:
```
!r5- 1+ 1 +1d7 - 2d10 + 2d10 + 1d10 ---- Inconsistent spacing
!r 5 - 1 + 1 + d7 - 2d10 + 2d10 + d10 ---- Missing number infront of dice (defaults to 1)
!r 5 / 1 * 1 + 1d7 * 2d10 / 2d10 + 2d10 ---- Why would you need to even do this???
!r 5 - 1 + 1 + 0d0 - 0d10 + 02d0 + 0d10 ---- Or this?
!r 1d99999999999999999 ---- Sure
```

## Running

Run the script like so:

```
python roller.py "!r 5 - 1 + 1 + 1d7 - 2d10 + 2d10 + d10"
This is what I was given !r 5 - 1 + 1 + 1d7 - 2d10 + 2d10 + d10
This is what I evaluated 5 - 1 + 1 + 5 - 18 + 13 + 1
Oi! the result is 6
```

That last line reminds me, the bot is [british](https://en.wikipedia.org/wiki/British). Don't screw up or he (his name is Lewis) *will* insult you:
```
This is what I was given !r 1 +- 1 + 1d7 - 2d10 + 2d10 +
Someone has Lost the plot.

This is what I was given !r a - 1 + 1 + 1d7 - 2d10 + 2d10 + d10
Daft Cow

This is what I was given !r _ + 1 + 1d7 - 2d10 + 2d10 +
Lazy Sod
```

Enjoy!


## Authors

* **Will Irwin** - *Everything* - [Upgwades](https://github.com/Upgwades)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Stackoverflow was very helpful
