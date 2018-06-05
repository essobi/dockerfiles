FROM slintes/alpine-glibc  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
RUN apk --update add tar bash && \  
curl -o /usr/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-amd64" && \  
chmod +x /usr/bin/gosu && \  
mkdir -p /opt/btsync && \  
curl -s -k -L "https://download-
cdn.getsyncapp.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz" | tar -xzf -
-C /usr/local/bin && \  
apk del tar && \  
rm -rf /var/cache/apk/*  
  
ADD
https://github.com/albertrdixon/tmplnator/releases/download/v2.2.1/t2-linux.tgz
/t2.tgz  
RUN tar -xvzf /t2.tgz -C /usr/local/bin && rm -vf /t2.tgz  
  
ENV USERID 1000  
ENV GROUPID 1000  
ADD configs /templates  
ADD scripts/* /usr/local/bin/  
RUN chmod a+rx /usr/local/bin/* &&\  
mkdir -p /data  
  
ENTRYPOINT ["docker-entry"]  
CMD ["docker-start"]  
  
EXPOSE 8888 3369  
ENV UI_PORT 8888  
ENV LISTEN_PORT 3369  
ENV USERNAME admin  
ENV PASSWORD admin  

