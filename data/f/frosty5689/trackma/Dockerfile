FROM python:3.6-alpine  
  
LABEL maintainer frosty5689 <frosty5689@gmail.com>  
  
RUN apk add --no-cache --update \  
ca-certificates \  
tzdata \  
&& update-ca-certificates \  
&& pip install --upgrade --no-cache-dir setuptools pyinotify envparse \  
&& rm -rf /root/.cache  
  
ARG TRACKMA_VERSION=master  
  
RUN apk add --no-cache --update --virtual build-dependencies wget unzip && \  
wget -O /tmp/trackma-$TRACKMA_VERSION.zip
https://github.com/z411/trackma/archive/$TRACKMA_VERSION.zip && \  
ls -l /tmp && \  
mkdir -p /opt && \  
unzip /tmp/trackma-$TRACKMA_VERSION.zip -d /opt && \  
mv /opt/trackma* /opt/trackma &&\  
cd /opt/trackma && \  
python setup.py develop && \  
rm -rf /tmp/trackma-$TRACKMA_VERSION.zip && \  
apk del build-dependencies  
  
ADD run/* /opt/trackma/  
  
VOLUME /config  
  
WORKDIR /opt/trackma  
  
CMD ["/opt/trackma/start.sh"]  

