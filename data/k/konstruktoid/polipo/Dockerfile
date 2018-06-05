FROM konstruktoid/debian:wheezy  
  
ENV USER polipo  
  
RUN \  
useradd \--system \--no-create-home \--user-group \--shell /usr/sbin/nologin
\--home-dir /bin proxy && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install polipo \--no-install-recommends && \  
apt-get -y clean && \  
useradd \--system \--no-create-home \--user-group \--shell /bin/false $USER &&
\  
rm -rf /var/lib/apt/lists/* \  
/usr/share/doc /usr/share/doc-base \  
/usr/share/man /usr/share/locale /usr/share/zoneinfo && \  
chown -R $USER:$USER /var/cache/polipo  
  
USER $USER  
EXPOSE 8123  
ENTRYPOINT ["/usr/bin/polipo"]  
CMD []  

