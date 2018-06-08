FROM alpine:latest  
MAINTAINER Jeroen Geusebroek <me@jeroengeusebroek.nl>  
  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm' \  
TIMEZONE='Europe/Amsterdam' \  
REFRESHED_AT='2018-03-09'  
RUN apk -U upgrade && \  
apk add --update tzdata && \  
apk -U add \  
ca-certificates bash sudo \  
py2-pip ca-certificates git python py-libxml2 py-lxml \  
make gcc g++ python-dev openssl-dev libffi-dev unrar \  
&& \  
pip --no-cache-dir install pyopenssl cheetah requirements && \  
git clone \--depth 1 https://github.com/SickRage/SickRage.git /sickrage && \  
apk del make gcc g++ python-dev && \  
rm -rf /tmp && \  
rm -rf /var/cache/apk/*  
  
VOLUME [ "/config" , "/downloads", "/cache"]  
  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
EXPOSE 8081  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ ""]

