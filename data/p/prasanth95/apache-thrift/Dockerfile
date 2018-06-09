FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -y install wget  
RUN wget http://mirror.fibergrid.in/apache/thrift/0.9.3/thrift-0.9.3.tar.gz  
RUN tar xvf thrift-0.9.3.tar.gz  
RUN cd thrift-0.9.3  
RUN apt-get -y install automake bison flex g++ git libboost1.55-all-dev
libevent-dev libssl-dev libtool make pkg-config  
RUN apt-get -y install ant  
RUN apt-get -y install default-jre  
RUN apt-get -y install default-jdk  
WORKDIR /thrift-0.9.3/lib/java/  
RUN ant  
WORKDIR /thrift-0.9.3  
RUN apt-get install python-all  
RUN apt-get -y install python-all-dev  
RUN apt-get -y install python-all-dbg  
RUN apt-get -y install python-twisted  
RUN apt-get install python-six  
RUN apt-get -y install python-pip  
WORKDIR /thrift-0.9.3/lib/py/  
RUN python setup.py install  
WORKDIR /thrift-0.9.3  
RUN apt-get -y install php5-dev  
RUN apt-get install php5-cli  
RUN apt-get -y install phpunit  
RUN ./configure  
RUN make  
RUN make install

