FROM alpine:3.6  
  
ENV LANG=en_US.UTF-8 LC_ALL=C.UTF-8 LANGUAGE=en_US.UTF-8  
  
ADD backup.sh /backup.sh  
ADD entrypoint.sh /entrypoint.sh  
  
RUN apk add --no-cache openssl-dev curl git build-base bash tar wget python
yajl yajl-dev cmake coreutils \  
&& git clone --branch master --single-branch
https://github.com/edenhill/kafkacat.git kafkacat \  
&& cd kafkacat \  
&& ./bootstrap.sh \  
&& make install \  
&& cd .. && rm -rf kafkacat \  
&& apk del curl git build-base bash tar wget python yajl-dev cmake coreutils \  
&& apk -Uuv add curl groff less python py-pip \  
&& pip install awscli \  
&& apk del py-pip \  
&& apk add bash \  
&& rm /var/cache/apk/* \  
&& chmod a+x backup.sh entrypoint.sh  
  
CMD ["/entrypoint.sh"]

