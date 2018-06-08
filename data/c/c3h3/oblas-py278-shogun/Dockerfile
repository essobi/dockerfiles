  
FROM c3h3/oblas-py278-data  
  
RUN apt-get update  
RUN apt-get -y install python2.7-dev python-all-dev  
RUN apt-get -y install swig  
  
RUN cd tmp/ && git clone https://github.com/shogun-toolbox/shogun.git  
RUN cd /tmp/shogun/ && mkdir build  
RUN cd /tmp/shogun/build && cmake -D BUNDLE_EIGEN=ON -D
PYTHON_EXECUTABLE=/root/.pyenv/versions/2.7.8/bin/python -D
PYTHON_INCLUDE_DIR=/root/.pyenv/versions/2.7.8/include/python2.7 -D
PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so -D
PYTHON_PACKAGES_PATH:PATH=/root/.pyenv/versions/2.7.8/lib/python2.7/site-
packages -D PythonModular=ON ..  
  
RUN cd /tmp/shogun/build && make && make install  
  
RUN cd /tmp && rm -rf shogun  
  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib  
  
VOLUME ["/ipynbs", "/data"]  
  

