##################################################################################################
# Python module for IDAPython scripts executed via idascript.
#
# Copied from the original idascript utility, with minor changes: http://www.hexblog.com/?p=128
#
# Craig Heffner
# 14-November-2012
# http://www.tacnetsol.com
# http://www.devttys0.com
##################################################################################################

import os
import sys
import tempfile
import idc
import idaapi
import idautils

class ToFileStdOut(object):
    def __init__(self, outfile):
        self.outfile = open(outfile, 'w')

    def write(self, text):
        self.outfile.write(text)

    def flush(self):
        self.outfile.flush()

    def isatty(self):
        return False

    def __del__(self):
        self.outfile.close()

# Redirect stdout and stderr to the output file
sys.stdout = sys.stderr = ToFileStdOut(os.path.join(tempfile.gettempdir(), 'ida_script_stdout.txt'))
# Make the normal sys.argv and sys.exit function properly
sys.argv = idc.ARGV
sys.exit = idc.Exit
# Wait for IDA's auto analysis to finish
idaapi.autoWait()

