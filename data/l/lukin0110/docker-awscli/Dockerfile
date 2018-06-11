#  
# Simple Alpine Python container with the AWS CLI included  
#  
FROM alpine:3.3  
RUN apk add --update \  
python \  
bash \  
py-pip \  
&& pip install awscli \  
&& rm -rf /var/cache/apk/*  
  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod ugo+x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

