# About #

IDAScript is a wrapper around IDA Pro that makes it easy to automate the execution of IDA scripts against target files from the command line. Scripts written for use with idascript can also be run manually in IDA's GUI without any code change.

This version of idascript is based on the original idascript from Hex-Rays, but is written in Python for platform independance (disclaimer: currently only tested on Linux!).

For more information on idascript, see the original idascript utility here: http://www.hexblog.com/?p=128

# Installation #

To install, run the included install.py script (typically requires root/admin privileges):

```
$ python ./install.py /path/to/ida/install/directory
```

On Linux/OSX platforms, idascript will be installed the first directory listed in $PATH.

On Windows, idascript will be placed in the specified IDA install directory.

# Scripts #

All IDAPython scripts intended for use with IDAScript must import the idascript Python module. If you want IDA to exit when the script is finished, the script must also call idascript.exit when done. Example:

```
import idascript

print "I am an IDA script. My first command line argument is:", sys.argv[1]

idascript.exit()
```

Scripts written in this manner can be used either through idascript utility or manually from inside the IDA GUI. The idascript module will detect when it is not being run via the idascript utility and will disable itself.

# Usage #

IDAScript usage is very straight forward:

```
$ idascript ./target.bin ./myscript.py arg1 arg2 arg3
```