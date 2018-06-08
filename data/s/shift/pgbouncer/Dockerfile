FROM shift/ubuntu:15.04  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
ADD ./pgbouncer_1.6.1-1_amd64.deb /tmp/pgbouncer_1.6.1-1_amd64.deb  
RUN apt-get update \  
&& apt-get install --yes libc-ares2 libevent-2.0-5 \  
&& dpkg -i /tmp/pgbouncer_1.6.1-1_amd64.deb \  
&& /usr/sbin/useradd postgres \  
&& id postgres  
  
USER postgres  
VOLUME /config  
EXPOSE 6432/tcp  
ENTRYPOINT ["pgbouncer", "/config/config.ini"]  

