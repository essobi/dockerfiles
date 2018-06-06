FROM lsiobase/alpine  
LABEL maintainer="sgtsquiggs"  
RUN \  
apk add \--no-cache \  
python2 \  
py2-pip \  
unrar &&\  
pip install --upgrade setuptools &&\  
pip install flexget rarfile  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config  

