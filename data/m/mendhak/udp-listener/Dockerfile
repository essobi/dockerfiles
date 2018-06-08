FROM gliderlabs/alpine:3.3  
MAINTAINER mendhak <docker@mendhak.com>  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/*  
  
ENV UDPPORT 5005  
ADD udplistener.py /udplistener.py  
CMD ["python", "-u","/udplistener.py"]  
  
EXPOSE ${UDPPORT}  
EXPOSE ${UDPPORT}/udp  

