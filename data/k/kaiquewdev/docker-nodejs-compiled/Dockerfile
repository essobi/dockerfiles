FROM ubuntu  
RUN apt-get -qq update  
RUN apt-get install -y software-properties-common python python-setuptools
build-essential wget  
RUN wget http://nodejs.org/dist/latest/node-v6.8.1.tar.gz  
RUN tar zxvf node-v6.8.1.tar.gz  
WORKDIR /node-v6.8.1  
RUN ./configure && make && make install  

