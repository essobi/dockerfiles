FROM alpine  
MAINTAINER Benoît Vidis <contact@benoitvidis.com>  
  
WORKDIR /opt  
RUN apk update \  
&& apk add git nodejs \  
&& git clone https://github.com/chmllr/NoteHub.git notehub \  
&& cd notehub \  
&& npm install \  
&& apk del git  
  
WORKDIR /opt/notehub  
CMD npm start  

