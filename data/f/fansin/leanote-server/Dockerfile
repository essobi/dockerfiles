# base mongo image  
#  
FROM mongo  
#  
MAINTAINER FansinZhao 171388204@qq.com  
  
# update and install wget ,use to download leanote-server binary file  
RUN set -ex; \  
\  
fetchDeps='ca-certificates wget'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
leanoteDownload="2.4/leanote-linux-amd64-v2.4.bin.tar.gz"; \  
wget -O leanote.bin.tar.gz "https://sourceforge.net/projects/leanote-
bin/files/$leanoteDownload/download"; \  
tar -zxvf leanote.bin.tar.gz; \  
rm -rf leanote.bin.tar.gz; \  
chown -R root:root /leanote; \  
\  
apt-get purge -y --auto-remove $fetchDeps  
#COPY leanote /leanote  
#copy run.sh  
COPY run.sh ./  
RUN chmod a+x /run.sh  
# resolve images not show  
RUN sed -i
's/site.url\=http\:\/\/localhost\:9000/site.url\=http\:\/\/172.17.0.2:9000/g'
/leanote/conf/app.conf  
#  
ENTRYPOINT ["/run.sh"]  
CMD []  

