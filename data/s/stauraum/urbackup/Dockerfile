FROM debian:stable-slim  
ENV VERSION 2.2.11  
MAINTAINER Kai Schubert <kai.schubert@systemmanager.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN apt-get update && apt-get install -y btrfs-tools apt-utils libguestfs-
tools \  
sqlite3 libcrypto++6 libcurl3 libfuse2 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
ADD https://hndl.urbackup.org/Server/${VERSION}/debian/stretch/urbackup-
server_${VERSION}_amd64.deb /root/install.deb  
RUN echo /var/urbackup | dpkg -i /root/install.deb && rm /root/install.deb  
  
# configure timezone  
RUN echo Europe/Berlin > /etc/timezone && dpkg-reconfigure tzdata  
  
EXPOSE 55413  
EXPOSE 55414  
EXPOSE 55415  
EXPOSE 35623  
VOLUME [ "/var/urbackup", "/var/log", "/usr/share/urbackup" ]  
ENTRYPOINT ["/usr/bin/urbackupsrv"]  
CMD ["run"]  

