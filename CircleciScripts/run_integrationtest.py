from functions import runcommand
from functions import runtest
from functions import TestTypes
from functions import getmodules
import sys
import os

test_results = sys.argv[1]
root = sys.argv[2]
credentials = sys.argv[3]
testmodules =  ["aws-android-sdk-mobile-client"]

runcommand('echo "export testresult=0" >> $BASH_ENV')  
runcommand("rm -rf {0}".format(test_results))
runcommand("mkdir {0}".format(test_results))
for module in testmodules:                      
    credentialfolder = os.path.join(root, module,"src/androidTest/res/raw")
    runcommand("mkdir -p '{0}'".format(credentialfolder))
    credentialfile=os.path.join(credentialfolder,"awsconfiguration.json")
    runcommand('cp "{0}" "{1}"'.format(credentials, credentialfile))
    if runtest(module, TestTypes.IntegrationTest, test_results) != 0:
        exit(1)
