FROM mback2k/ubuntu:rolling  
  
RUN adduser --disabled-password --disabled-login --system --group \  
\--uid 9987 --home /data teamspeak3  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
mariadb-client libmariadb2 \  
locales bzip2 && \  
apt-get clean  
  
RUN locale-gen en_US en_US.UTF-8 && dpkg-reconfigure locales  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  
RUN mkdir -p /app  
WORKDIR /app  
  
ADD
http://dl.4players.de/ts/releases/3.0.13.8/teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2
/app  
RUN tar xfvj teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2  
  
RUN chown root:root -R /app/teamspeak3-server_linux_amd64  
RUN chown teamspeak3:teamspeak3 /app/teamspeak3-server_linux_amd64  
  
RUN ln -s /app/teamspeak3-server_linux_amd64 /app/teamspeak3  
WORKDIR /app/teamspeak3  
  
VOLUME /data  
  
EXPOSE 9987/udp 10011/tcp 30033/tcp  
  
ENV TEAMSPEAK3_APPDIR /app/teamspeak3  
ENV TEAMSPEAK3_INIFILE /data/ts3server.ini  
  
ADD docker-entrypoint.d/ /run/docker-entrypoint.d/  
  
CMD ["/usr/local/bin/teamspeak3"]  

