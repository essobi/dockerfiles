FROM debian:stable  
MAINTAINER Tabulo <dev@tabulo.net>  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV VERSION 2.1.20  
ENV FILE urbackup-server_${VERSION}_amd64.deb  
ENV URL
https://www.urbackup.org/downloads/Server/${VERSION}/debian/stable/${FILE}  
  
ADD ${URL} /root/${FILE}  
  
RUN apt-get update \  
&& echo "/var/urbackup" | apt-get install -f -y /root/${FILE} \  
&& rm /root/${FILE} && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 55413  
EXPOSE 55414  
EXPOSE 55415  
EXPOSE 35623  
VOLUME [ "/var/urbackup", "/var/log", "/usr/share/urbackup",
"/srv/urbackup/backups" ]  
ENTRYPOINT ["/usr/bin/urbackupsrv"]  
CMD ["run"]  

