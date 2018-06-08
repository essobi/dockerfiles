FROM alpine  
MAINTAINER Ivan Yaroslavov Stefanov <ivan.yaroslavov@vne.io>  
  
ARG SRC_FOLDER=/opt/vne-graphite-src  
ARG CONF_FOLDER=/opt/graphite/conf  
ARG LOG_FOLDER=/var/log/supervisor  
  
COPY . $SRC_FOLDER  
  
RUN apk update \  
&& apk add python \  
&& apk add py-pip \  
&& apk add python-dev \  
&& apk add supervisor \  
&& apk add build-base \  
&& export PYTHONPATH="/opt/graphite/lib/" \  
&& pip install 'Twisted<12.0' \  
&& pip install https://github.com/graphite-project/whisper/tarball/master \  
&& pip install https://github.com/graphite-project/carbon/tarball/master \  
&& mkdir $LOG_FOLDER \  
&& mv $SRC_FOLDER/supervisord.conf /etc \  
&& mv $SRC_FOLDER/carbon.conf $CONF_FOLDER \  
&& mv $SRC_FOLDER/storage-schemas.conf $CONF_FOLDER  
  
EXPOSE 2003  
CMD /usr/bin/supervisord  
  

