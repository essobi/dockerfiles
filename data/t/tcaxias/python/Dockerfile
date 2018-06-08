FROM alpine:edge  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
  
RUN \  
apk --update \--no-cache add python3 && \  
ln -s $(which python3) /usr/local/bin/python && \  
easy_install-3.5 pip && \  
pip install --upgrade pip  

