# six-nibble-name

A minimal, light-weight Python module for converting six nibbles (three bytes) into a
4-character name.

## How To

The `sixnibblename` module contains a single function: `get()`. This takes either zero
or one arguments, depending on your use case.
* If you just want to convert six nibbles into a name on Python (micro or regular),
  pass in the number (ideally a 6 nibble integer) as an argument to the `get()` function
  and it will be converted to a 4 byte name
  * If the integer being converted has more than 6 nibbles, only the lowest 6 will be used
* On Micropython, simply call the `get()` function argumentless to get the name of
  the device based on the unique id of the device

Here is a full example, showing outputs of pre-set integers being converted:

```python
>>> import sixnibblename
>>> sixnibblename.get(0x123456)
'Mori'
>>> sixnibblename.get(0x32123456)
'Mori'
>>> sixnibblename.get()
'Dura'
>>> name = sixnibblename.get()
>>> print('Hello, my name is %s' % name)
Hello, my name is Dura
```

## But...why?

The idea behind the design of this module is to convert somewhat unique, ugly names (such as
those retrieved through the [ESP8266 Micropython unique_id() call](http://docs.micropython.org/en/v1.9.3/esp8266/library/machine.html#machine.unique_id))
into something not only readable, but memorable.

I appreciate that in the process of making something readable, I have also
made the identifier even less unique than it was originally, however the use case for this
sort of naming system is small, local networks (think less than 10 devices), in which case
the odds of one device having the same name as another is less than 0.2%. If you think this
is possibly going to be an issue for you, please do not use this module!

I also recognise that the values are slightly weighted towards some values than others
(more substantial on the vowels than consonants). If someone wants to help improve the
algorithm for a more even distribution, please throw me PR!


## Closing Statements

If you really wish your devices had a bit more of a personality, and aren't overly concerned
about the uniqueness or clashes, this may be the perfect module for you.
