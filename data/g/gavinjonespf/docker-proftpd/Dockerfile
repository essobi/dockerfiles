FROM ubuntu:xenial  
  
RUN apt-get update -y && apt-get install -y proftpd curl  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY proftpd.conf /etc/proftpd/proftpd.conf  
#RUN sudo chown root:root /etc/proftpd/proftpd.conf  
RUN mkdir /ftp  
  
#Use GOSU  
# ENV GOSU_VERSION 1.7  
# RUN set -x \  
# && curl -sSLo /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
# && curl -sSLo /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
# && export GNUPGHOME="$(mktemp -d)" \  
# && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
# && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
# && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
# && chmod +x /usr/local/bin/gosu \  
# && gosu nobody true  
  
ENV PROFTPD_SERVERNAME proftpd  
ENV PROFTPD_RUNASUSER root  
ENV PROFTPD_ALLOWROOT off  
ENV PROFTPD_ALLOWOVERWRITE on  
#ENV PROFTPD_ARGS  
ENV PROFTPD_DEBUGLEVEL 0  
#Default to no UID translation  
#ENV PROFTPD_UID 1000  
ENV PROFTPD_PASSIVE_MIN 4999  
ENV PROFTPD_PASSIVE_MAX 50000  
ENV PROFTPD_DEFAULT_ADDR 0.0.0.0  
ENV PROFTPD_HOMEDIR /ftp  
  
EXPOSE 21  
EXPOSE 20  
EXPOSE 50000  
  
ENTRYPOINT /docker-entrypoint.sh  

