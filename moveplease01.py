#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/')
shutil.move('raynor.obj', 'ceph_storage/')
xname = input("what is new name for kerrigan.obj? ")
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
