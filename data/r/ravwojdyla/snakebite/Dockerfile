FROM uggedal/alpine  
MAINTAINER Rafal Wojdyla "ravwojdyla@gmail.com"  
RUN apk add -U && apk add python=2.7.8-r0 curl  
RUN curl https://bootstrap.pypa.io/ez_setup.py | python  
RUN easy_install snakebite  
  
ENTRYPOINT ["snakebite"]  

