# six-byte-name

A minimal, light-weight Python module for converting six bytes into a 4-character name.

## How To

The `sixbytename` module contains a single function: `get`. This takes a single argument,
ideally a 6 byte integer, and converts it to a 4 character string designed to be memorable.

If the integer being converted has more than 6 bytes, only the lowest 6 bytes will be used.

Here is a full example, showing outputs of pre-set integers being converted:

```python
>>> import sixbytename
>>> sixbytename.get(0x123456)
'Mori'
>>> sixbytename.get(0x32123456)
'Mori'
>>> name = sixbytename.get(0x234567)
>>> print('Hello, my name is %s' % name)
Hello, my name is Waci
```

## But...why?

The idea behind the design of this module is to convert somewhat unique, ugly names (such as
those retrieved through the [ESP8266 Micropython unique_id() call](http://docs.micropython.org/en/v1.9.3/esp8266/library/machine.html#machine.unique_id))
into something not only readable, but memorable. Please note that the `unique_id()`
call mentioned above returns a byte string, not an int, so this will not work directly,
you'll need to convert that to an int first! An untested attempt at doing so:
`int(machine.unique_id(), 16)`

I appreciate that in the process of making something readable, I have also
made the identifier even less unique than it was originally, however the use case for this
sort of naming system is small, local networks (think less than 10 devices), in which case
the odds of one device having the same name as another is less than 0.1%. If you think this
is possibly going to be an issue for you, please do not use this module!

I also recognise that the values are slightly weighted towards some values than others
(more substantial on the vowels than consonants). If someone wants to help improve the
algorithm for a more even distribution, please throw me PR!

On the other hand, if you really wish your devices had a bit more of a personality,
and aren't overly concerned about the uniqueness or clashes, this may be the perfect module
for you.
