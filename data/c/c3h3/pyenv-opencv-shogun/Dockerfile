  
FROM c3h3/pyenv-opencv:agilearning  
  
MAINTAINER Chia-Chi Chang <c3h3.tw@gmail.com>  
  
RUN apt-get update && apt-get -y install swig  
  
RUN cd /tmp/ && git clone https://github.com/shogun-toolbox/shogun.git && cd
/tmp/shogun/ && mkdir build && cd /tmp/shogun/build && cmake -D
BUNDLE_EIGEN=ON -D PYTHON_EXECUTABLE=/root/.pyenv/versions/2.7.8/bin/python -D
PYTHON_INCLUDE_DIR=/root/.pyenv/versions/2.7.8/include/python2.7 -D
PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so -D
PYTHON_PACKAGES_PATH:PATH=/root/.pyenv/versions/2.7.8/lib/python2.7/site-
packages -D PythonModular=ON .. && cd /tmp/shogun/build && make && make
install && cd /tmp && rm -rf shogun  
  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib  

