FROM alpine:latest  
LABEL maintainer "DI GREGORIO Nicolas <nicolas.digregorio@gmail.com>"  
  
### Environment variables  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm'  
### Install Application  
RUN apk upgrade --no-cache && \  
apk add --no-cache --virtual=run-deps \  
su-exec \  
python \  
git && \  
mkdir -p /opt/ && \  
git clone \--depth 1 https://github.com/rembo10/headphones.git /opt/headphones
&& \  
rm -rf /opt/headphones/.git \  
/tmp/* \  
/var/cache/apk/* \  
/var/tmp/*  
  
# Expose volumes  
VOLUME ["/config","/audio"]  
  
# Expose ports  
EXPOSE 8181  
### Running User: not used, managed by docker-entrypoint.sh  
#USER headphones  
### Start headphones  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["headphones"]  

