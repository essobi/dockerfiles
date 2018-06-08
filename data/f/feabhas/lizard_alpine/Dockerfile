FROM gliderlabs/alpine:3.3  
ENV REFRESHED_AT 2018-01-31  
RUN apk add --update --no-cache \  
python \  
py-pip \  
&& pip install --upgrade pip \  
&& pip install lizard  
  
WORKDIR /usr/project  
  

