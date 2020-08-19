import os
import shutil
from config import gin_dir


# copy gin.jar and quixbugs folder from gin project directory
# and overwrite into current folder
def copy_resources():
    # copy and overwrite gin.jar
    dst_jar = 'gin.jar'
    src_jar = '{}/build/{}'.format(gin_dir, dst_jar)
    shutil.copyfile(src_jar, dst_jar)
    print('copy and overwrite gin.jar')

    # copy and overwrite quixbugs
    dst_quixbugs = 'quixbugs'
    src_quixbugs = '{}/{}'.format(gin_dir, dst_quixbugs)
    if os.path.exists(dst_quixbugs):
        shutil.rmtree(dst_quixbugs)
    shutil.copytree(src_quixbugs, dst_quixbugs)
    print('copy and overwrite quixbugs')


if __name__ == '__main__':
    copy_resources()
