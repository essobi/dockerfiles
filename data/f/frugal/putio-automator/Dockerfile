FROM alpine:latest  
MAINTAINER Andrew Dacey <adacey@gmail.com>  
# Setup directories  
RUN mkdir -p /config  
ENV HOME /config  
# Install basic dependencies  
RUN apk update && apk upgrade && apk add \--no-cache \  
bash \  
python \  
py-pip  
RUN pip install --no-cache-dir putio-automator  
RUN cp /usr/share/putio-automator/config.py.dist /config/config.py  
RUN mkdir -p /files/incomplete  
ADD putio.sh /usr/bin/putio.sh  
WORKDIR /config  
VOLUME ["/config","/files/downloads","/files/torrents","/files/incomplete"]  
ENTRYPOINT ["putio.sh"]  

