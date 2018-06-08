FROM nimmis/alpine-micro  
  
MAINTAINER nimmis <kjell.havneskold@gmail.com>  
  
  
RUN apk update && apk upgrade && \  
apk add python3 && \  
ln -sf `which python3` /usr/bin/python && \  
apk add \--virtual=build-dependencies curl && \  
curl https://bootstrap.pypa.io/get-pip.py | python3 && \  
apk del build-dependencies && \  
rm -Rf /root/.cache && \  
rm -rf /var/cache/apk/*  
  
  

