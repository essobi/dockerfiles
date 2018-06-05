FROM alpine:3.2  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
VOLUME ["/data"]  
ENTRYPOINT ["docker-entry"]  
CMD ["docker-start"]  
EXPOSE 8081  
ENV OPEN_FILE_LIMIT 32768  
ENV PATH /usr/local/bin:$PATH  
ENV SB_DATA /data  
ENV SB_HOME /sickrage  
ENV SB_PORT 8081  
ENV SB_USER root  
ENV SICKRAGE_CHANNEL master  
ENV SUPERVISOR_LOG_LEVEL INFO  
ENV UPDATE_INTERVAL 4h  
  
ADD
https://github.com/albertrdixon/tmplnator/releases/download/v2.2.1/t2-linux.tgz
/t2.tgz  
RUN tar xvzf /t2.tgz -C /usr/local/bin  
  
ADD
https://github.com/albertrdixon/escarole/releases/download/v0.1.1/escarole-
linux.tgz /es.tgz  
RUN tar xvzf /es.tgz -C /usr/local \  
&& ln -s /usr/local/bin/escarole-linux /usr/local/bin/escarole \  
&& rm -f /es.tgz  
  
ADD bashrc /root/.profile  
ADD gitconfig /root/.gitconfig  
ADD configs /templates  
ADD scripts/* /usr/local/bin/  
RUN chown root:root /usr/local/bin/* \  
&& chmod a+rx /usr/local/bin/* \  
&& mkdir /torrents /tv_shows /downloads  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add \  
bash \  
ca-certificates \  
git \  
py-html5lib \  
py-lxml \  
py-mako \  
py-openssl \  
py-pillow \  
python \  
supervisor \  
unrar  
  
RUN git clone -v --depth 1 git://github.com/SickRage/SickRage.git /sickrage  

