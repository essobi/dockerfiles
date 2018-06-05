FROM alpine:3.6  
RUN apk add --update python py-pip \  
&& pip install --upgrade pip \  
&& pip install awscli  
  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  

