FROM alpine  
MAINTAINER "Romain Acciari" <romain.acciari@openio.io>  
  
RUN apk add --no-cache py-virtualenv git sudo gcc python2-dev python2-dev \  
libc-dev libxml2-dev libxslt-dev  
RUN git clone https://github.com/ceph/s3-tests.git \  
&& cd s3-tests \  
&& ./bootstrap  
  
ADD nosetests.sh config /  
  
ENTRYPOINT ["/nosetests.sh"]  

