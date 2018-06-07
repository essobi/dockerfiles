#Dictionary Server  
#version 0.0.1  
#use the fedora base image provided by dotCloud  
FROM fedora  
  
MAINTAINER Hipin Zhao "zhaohaibin@outlook.com"  
#make sure the package repository is up to date.  
RUN yum update -y  
RUN yum upgrade -y  
  
#install wget telnet git vim unzip  
RUN yum install wget telnet git vim unzip -y  
  
#install compile envirement  
RUN yum install gcc gcc-c++ automake libtool -y  
  
#install boost library  
RUN yum install boost-devel boost-date-time boost-filesystem boost-iostreams
boost-locale boost-log boost-regex boost-serialization boost-system -y  
  
#install postgresql-devel postgresql93 client  
RUN rpm -Uvh http://yum.postgresql.org/9.3/fedora/fedora-20-x86_64/pgdg-
fedora93-9.3-1.noarch.rpm  
  
RUN yum install postgresql93-devel postgresql93 -y  
  
#compile third library  
#clone libuv  
RUN git clone https://github.com/joyent/libuv.git /tmp/libuv  
  
#workdir for libuv compile  
WORKDIR /tmp/libuv  
RUN sh autogen.sh && ./configure && make && make install  
  
#link libuv to /usr/lib64  
RUN ln -s /usr/local/lib/libuv.so.11 /usr/lib64/libuv.so.11  
  
#tmp workdir  
WORKDIR /tmp  
  
#download libxls  
RUN wget http://softlayer-
ams.dl.sourceforge.net/project/libxls/libxls-1.4.0.zip  
RUN /usr/bin/unzip -x libxls-1.4.0.zip  
  
#workdir for libxls  
WORKDIR /tmp/libxls  
  
#compile libxls  
RUN ./configure && make && make install  
  
#change to workdir to /tmp  
WORKDIR /tmp  
  
#clone dictionaryonline  
RUN git clone https://github.com/haibinpark/DictionaryOnline.git  
  
#change to workdir to /tmp/DictionaryOnline  
#update repository  
WORKDIR /tmp/DictionaryOnline  
RUN git pull  
  
#compile  
WORKDIR /tmp/DictionaryOnline/make  
RUN make server  
RUN mkdir -p /usr/local/bin  
RUN mv ./dictionaryserver /usr/local/bin/ds  
  
#change to old workdir  
WORKDIR /  
  
#add run shell script  
ADD run.sh /usr/local/bin/run.sh  
  
#exec run shell script  
CMD [/usr/local/bin/run.sh]  

