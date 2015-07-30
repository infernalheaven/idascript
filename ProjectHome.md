IDAScript is a wrapper around IDA Pro that makes it easy to automate the execution of IDA scripts against target files from the command line. Scripts written for use with idascript can also be run manually in IDA's GUI without any code change.

Example code to find all cross-references to strcpy:

```
import idascript

print "Cross references to strcpy:"

for xref in XrefsTo(LocByName("strcpy")):
    print "0x%.8X  %s" % (xref.frm, GetDisasm(xref.frm))

idascript.exit()
```