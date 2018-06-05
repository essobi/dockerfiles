FROM alpine:edge  
MAINTAINER XForce <hello@web.com>  
  
RUN apk --update --no-cache add \  
bash aria2  
  
#RUN set -xe \  
# && rm -rf /var/cache/apk/* \  
# && aria2c https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64 -o
/usr/local/bin/gosu \  
# && chmod +x /usr/local/bin/gosu  
#RUN addgroup aria2 && adduser -s /bin/bash -D -G aria2 aria2  
VOLUME /download  
VOLUME /conf  
EXPOSE 6800  
#COPY run.sh /run.sh  
#CMD ["bash", "/run.sh"]  
CMD ["bash", "/conf/run_aria2_docker.sh"]  
#CMD set -xe \  
# && chmod -R 777 /download \  
# && chmod -R 777 /conf \  
# && gosu aria2 aria2c --conf-path=/conf/aria2.conf  

