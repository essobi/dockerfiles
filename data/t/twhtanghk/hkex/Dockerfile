FROM node  
  
ENV VER=${VER:-master} \  
REPO=https://github.com/twhtanghk/hkex \  
APP=/usr/src/app  
  
RUN apt-get update \  
&& apt-get install -y git \  
&& apt-get clean  
  
RUN git clone -b $VER $REPO $APP  
  
WORKDIR $APP  
RUN npm install  

