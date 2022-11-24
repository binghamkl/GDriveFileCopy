import os
import time
from datetime import datetime

# Module to copy files from a source directory to a Google drive folder if they've been updated.


def SyncAndCopyFiles(Source : str, Destination : str) : 
    '''
        Syncs all source files into Destination on google drive.
    '''
    print(Source, flush=True)
    print(Destination, flush=True)


    files = os.listdir("/source")

    fh = open(os.path.join("/source", "filelist.txt"), "w")
    fh.write(Source + "\n")
    fh.write(Destination + "\n")
    fh.write ("\n".join(files))
    fh.close

source = os.getenv("Source", ".")
destination = os.getenv("Destination", ".")

SyncAndCopyFiles(source, destination)
while True:
    time.sleep(1)
    print(datetime.now(), flush=True)