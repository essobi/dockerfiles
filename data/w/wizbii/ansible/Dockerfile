FROM williamyeh/ansible:alpine3  
  
RUN apk add \--update alpine-sdk python-dev \  
&& pip install apache-libcloud pycrypto \  
&& apk del alpine-sdk python-dev  

