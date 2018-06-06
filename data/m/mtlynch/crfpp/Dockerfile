FROM ubuntu:16.04  
LABEL maintainer="Michael Lynch <michael@mtlynch.io>"  
  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y build-essential git python2.7 python-pip && \  
pip install --upgrade pip  
  
ADD . /crfpp  
WORKDIR /crfpp  
  
RUN ./configure && \  
make && \  
make install && \  
echo "/usr/local/lib" > /etc/ld.so.conf.d/local.conf && \  
ldconfig  
  
# Clean up.  
RUN rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/doc && \  
rm -rf /usr/share/man && \  
apt-get autoremove -y && \  
apt-get clean  

