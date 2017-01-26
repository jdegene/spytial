# -*- coding: utf-8 -*-

import os


class osfuncs():
    """
    Handles all data_functions that take care of os level file changes
    """
    
    #if curDir already exists, delete it and recreate it
    def chkdir(curDir):
        if os.path.isdir(curDir):
            try:
                os.remove(curDir)
            except:
                print("Folder exists but cannot be deleted")
        try:
            os.mkdir(curDir)
        except:
            print("Cannot create Folder: ", curDir)
        
        return curDir
    
    #if curDir already exists, do nothing, else create it
    def chkdir2(curDir):
        if os.path.isdir(curDir):
            return
        else:
            try:
                os.mkdir(curDir)
            except:
                print("Cannot create Folder: ", curDir)
            
        return curDir
    



class Landsat(object):
    """
    Provides all means to download, store, process and manipulate Landsat data
    """
    
    def __init__(self, mainFol):
        """Landsat objects handle subfolders in the main folder """
        self.tarFol = False