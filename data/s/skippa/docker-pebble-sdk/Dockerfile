FROM ubuntu  
MAINTAINER mike.aizatsky@gmail.com  
  
ENV PEBBLE_SDK_VERSION 4.1.4  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y git curl  
RUN apt-get install -y libfreetype6-dev  
RUN apt-get install -y gcc-arm-none-eabi python python-pip python-dev nodejs
npm  
RUN pip install --upgrade pip  
RUN pip install virtualenv  
  
RUN git clone https://github.com/pebble/pebble-tool.git /tool  
WORKDIR /tool  
RUN pip install -r requirements.txt && rm /root/.cache/ -r  
  
RUN mkdir -p /root/.pebble-sdk/ && \  
touch /root/.pebble-sdk/ENABLE_ANALYTICS  
  
COPY pebble /usr/local/bin/  
RUN yes | pebble sdk install $PEBBLE_SDK_VERSION  
  
WORKDIR /  
CMD pebble --help  
  

