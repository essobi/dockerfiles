FROM ubuntu:14.04  
#  
# This instructions are from  
# https://slack-files.com/T02FPGBKB-F0KJU1CLX-cbbcf8a02c  
#  
WORKDIR /tmp  
  
#Install git and multiple dependencies  
RUN apt-get update && apt-get -y upgrade && \  
apt-get install -y git build-essential \  
libssl-dev libffi-dev python-dev openssl \  
python-pip libzmq3-dev  
  
#Install libsodium-dev  
RUN echo "deb http://ftp.de.debian.org/debian sid main" | tee -a
/etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get -y --force-yes upgrade  
RUN apt-get install -y --force-yes libsodium-dev  
  
#Install cryptography  
RUN pip install cryptography  
  
#Install libzmq  
RUN apt-get install -y --force-yes autoconf pkg-config libtool  
  
RUN git clone https://github.com/zeromq/libzmq  
  
RUN cd libzmq && ./autogen.sh && ./configure && make -j 4 && \  
make install && ldconfig  
  
## Installing the Server  
# Git clone the OpenBazaar server repository somewhere on your computer  
RUN git clone https://github.com/OpenBazaar/OpenBazaar-Server.git /server  
  
# Navigate to the newly created folder  
WORKDIR /server  
  
# Install other dependencies  
RUN pip install -r requirements.txt  
RUN pip install -r test_requirements.txt  
  
# Setup authentication  
ADD run.sh /server/run.sh  
  
RUN chmod 300 run.sh  
  
CMD ["./run.sh"]  

