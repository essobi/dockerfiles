FROM alpine  
  
RUN apk add --update \  
ca-certificates \  
python \  
py-pip \  
groff \  
less \  
&& rm -rf /var/cache/apk/*  
  
RUN pip install awscli  
  
COPY config /root/.aws/config  
  
CMD [ "aws" ]  

