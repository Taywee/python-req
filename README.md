# python-req
Simple python module for loading and dumping structures in req format, a very
simple {string: (string|list(string))} format.

Parses a structure like this:

```
Foo|Bar
Baz_1|alpha
Baz_2|beta
Baz_3|gamma
```

into
    
```python
{
    'Foo': 'Bar',
    'Baz': [
        'alpha',
        'beta',
        'gamma',
    ],
}
```

The load and dump methods will maintain the encoding given and will not correct
on errors.  If you pass a utf-8 filehandle to load, you'll get unicode output.
If you pass a bytestring filehandle to load, you'll get bytestring output.
loads is the same, but with either a unicode or bytestring input.  dump will try
to do the same, and dumps will attempt to determine the type.  All dicts and
arrays are expected to be entirely homogeneous (either entirely composed of
unicode strings or entirely composed of byte strings).  To not enforce this in
the client side is undefined, and may be an explicit error in the future.
Another undefined action is to embed newlines in any strings.

The only truly ambiguous case is dumps when given an empty dict.  In this case,
dumps will return an empty str object, which is unicode on Python 3 and bytes on
Python 2.

For structures parsed into lists, the logic is as such:

* Any underscore and non-negative integer ending a key will automatically coerce
  into an list.
* The actual values of the integers aren't important.  They will be ordered
  based on their decimal order.  Holes and starting index aren't bothered with.
* If a field has an integer index given, but also has a non-indexed field of the
  same name, the non-indexed field will be given top precedence (essentially an
  index of -1)
* Output of lists is 1-indexed by default, but this may be changed via a kwarg.
  If you need holes for whatever reason, you should pre-process the arrays into
  regular dict mappings.

This format is order-independent by default, but you may use an OrderedDict or
something to maintain order on reading and writing.  This does mean that dumping
and loading an object (or vice versa) aren't guaranteed to yield the exact same
representation, but doing any 3 alternating operations in a row usually should.
