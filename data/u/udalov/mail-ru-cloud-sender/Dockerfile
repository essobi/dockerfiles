FROM buildpack-deps:stretch  
  
MAINTAINER Sergei O. Udalov <sergei.udalov@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y -qq git cmake g++ libfuse-dev libcurl4-gnutls-dev
libjsoncpp-dev glusterfs-client  
  
RUN git clone https://gitlab.com/Kanedias/MARC-FS.git /usr/local/src/marc-fs
&& \  
cd /usr/local/src/marc-fs && git submodule init && git submodule update && \  
mkdir /usr/local/src/marc-fs/build && \  
cd /usr/local/src/marc-fs/build && cmake .. && make && \  
mv /usr/local/src/marc-fs/build/marcfs /usr/local/bin/  
  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY mount-mail-ru.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/*  
  
RUN adduser --system app  
USER app  
  
RUN mkdir /tmp/mailru  
RUN mkdir /tmp/cache  
  
ENV MAILRU_LOGIN=example@mail.ru  
ENV MAILRU_PASSWORD=example@mail.ru  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["bash"]  

