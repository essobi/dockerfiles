FROM ubuntu:16.04  
MAINTAINER filippocucchetto@gmail.com  
  
# Install dependencies  
RUN apt-get update && apt-get install -y build-essential wget git cmake xvfb
lcov ruby  
# Install coverall  
RUN gem install coveralls-lcov  
# Clone google test  
RUN cd && git clone https://github.com/google/googletest.git  
# Install google test  
RUN cd ~/googletest && git checkout 82febb8eafc0425601b0d46567dc66c7750233ff
&& mkdir build && cd build && cmake .. && make -j16 && make install  
# Copy build file to root directory  
COPY build.sh /root  

