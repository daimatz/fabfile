from fabric.api import task

import sys
sys.path.append('software')

import base
import haskell

@task
def all():
    '''
# all
    '''
    base.all()
    haskell.all()
