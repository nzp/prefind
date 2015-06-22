Logfind
========
A simple grep-like tool to find files containing one or more strings.

Usage
------
Logfind reads configuration from ``~/.logfind`` (by default) to figure out in
which files to look for the strings.  The format of this file is simple:

1. Each *absolute* file path on a line by itself.
2. Paths are specified as `Python regular expressions`_.
3. Blank lines (lines containing only white space characters) are ignored.
4. Lines beginning with ``#`` are comments and are also ignored.

To use the program, run::

        logfind [-o] [regex [regex ...]]

String(s) to match are specified as `Python regular expressions`_ just like
file paths are.

The program has one option:

-o      Instead of the default regex chaining (logical ``AND``), use logical
        ``OR`` chaining.

The output is a list of file paths containing the specified regular
expression(s), each on a separate line.


.. _Python regular expressions: https://docs.python.org/2/howto/regex.html