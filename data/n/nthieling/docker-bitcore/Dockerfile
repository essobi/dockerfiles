FROM ubuntu:xenial  
MAINTAINER Nick Thieling <nick@adrift.io>  
  
# EXPOSE 3001 3232 6667 8333 18333 # specify ports at runtime based on
services used  
HEALTHCHECK \--interval=5s --timeout=5s --retries=10 CMD curl -f
http://localhost:3001/insight/  
  
RUN apt-get update && apt-get install -y \  
libzmq3-dev \  
build-essential \  
python2.7 \  
curl  
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -y nodejs  
RUN npm install bitcore@4.1.0 -g  
  
ENTRYPOINT [ "bitcored" ]  

