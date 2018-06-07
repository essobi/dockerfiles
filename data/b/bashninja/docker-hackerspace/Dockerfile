FROM lsiobase/alpine.python:3.7  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
LABEL maintainer="Mike Weaver"  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN \  
echo "**** install packages ****" && \  
apk add --no-cache \  
python \  
py-mysqldb && \  
# sqlite && \  
echo "**** install temp packages ****" && \  
apk add --virtual _build-packages_ \  
alpine-sdk \  
python-dev && \  
#echo "**** install pip packages ****" && \  
pip install --no-cache-dir -U \  
pytz \  
django==1.5.12 \  
django-recaptcha \  
braintree && \  
#echo "**** cleanup ****" && \  
#apk del --purge _build-packages_ && \  
rm -rf /var/cache/apk/* && \  
rm -rf \  
/root/.cache \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config  
  
EXPOSE 8181

