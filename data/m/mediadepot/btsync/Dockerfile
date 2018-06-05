FROM mediadepot/base  
  
#Create couchpotato folder structure & set as volumes  
RUN mkdir -p /srv/btsync/app && \  
mkdir -p /srv/btsync/config && \  
mkdir -p /srv/btsync/data  
  
WORKDIR /srv/btsync/app  
  
RUN wget "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk" \  
"https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-
bin-2.21-r2.apk" && \  
apk add --allow-untrusted glibc-2.21-r2.apk glibc-bin-2.21-r2.apk && \  
/usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
rm /var/cache/apk/*  
  
#start.sh will download the latest version of btsync and run it.  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
  
VOLUME [ "/srv/btsync/config", "/srv/btsync/data"]  
  
# Web GUI  
EXPOSE 8888  
# Listening port  
EXPOSE 55555  
CMD ["/srv/start.sh"]

