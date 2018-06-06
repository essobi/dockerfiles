FROM alpine  
  
LABEL maintainer="Filip Tepper https://github.com/filiptepper/docker-yelp-
elastalert"  
RUN mkdir -p /etc/elastalert  
  
RUN apk update && \  
apk upgrade && \  
apk add libc6-compat py2-pip gcc python2-dev musl-dev libffi-dev openssl-dev
&& \  
pip install elastalert==0.1.26 rollbar  
  
VOLUME /etc/elastalert  
  
CMD PYTHONPATH="$PYTHONPATH:/etc/elastalert" elastalert --config
/etc/elastalert/config.yaml  

