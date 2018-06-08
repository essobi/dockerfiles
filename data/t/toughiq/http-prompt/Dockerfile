FROM python:alpine  
MAINTAINER toughiq@gmail.com  
  
RUN apk update && apk upgrade \  
&& pip install http-prompt  
  
ENTRYPOINT ["http-prompt"]  

