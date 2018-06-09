FROM ubuntu:precise  
  
RUN apt-get -qq update && \  
apt-get -qqy install \  
build-essential \  
cmake \  
doxygen \  
graphviz \  
libgtkmm-3.0-dev \  
net-tools \  
netcat \  
unzip \  
valgrind  
  
WORKDIR /code  
  
ADD cpplint /usr/local/bin/cpplint  
ADD cpplint.py /usr/local/bin/cpplint.py  
ADD filter_options /usr/local/bin/filter_options  
  
RUN chmod a+x /usr/local/bin/cpplint  
  
CMD ["make"]  

