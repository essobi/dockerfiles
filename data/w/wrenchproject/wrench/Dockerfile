FROM wrenchproject/wrench-build:ubuntu-xenial-gcc5  
  
MAINTAINER Rafael Ferreira da Silva <rafsilva@isi.edu>  
  
#################################################  
# INSTALL WRENCH  
#################################################  
  
USER root  
WORKDIR /tmp  
  
# install WRENCH  
RUN git clone https://github.com/wrench-project/wrench && cd wrench && mkdir
build && cd build && cmake .. && make && sudo make install  
  
# copy examples  
RUN cp -R wrench/build/examples/simple-example/workflow_files /home/wrench &&
cp -R wrench/build/examples/simple-example/platform_files /home/wrench  
RUN chown -R wrench /home/wrench  
  
# remove installation folder  
RUN rm -rf wrench  
  
#################################################  
# WRENCH's user  
#################################################  
  
USER wrench  
WORKDIR /home/wrench  
  
# set user's environment variable  
ENV CXX="g++-5" CC="gcc-5"  
ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib  

