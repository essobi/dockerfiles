FROM centos:7.3.1611  
MAINTAINER KingKwan <kmkim@bitnine.net>  
  
RUN yum -y install util-linux && \  
groupadd -r agraph --gid=9999 && \  
useradd -r -g agraph --uid=9999 agraph && \  
yum clean all && \  
ln -s /usr/lib64/libpython2.7.so.1.0 /usr/lib64/libpython2.6.so.1.0 && \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && \  
curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc" && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm -f /usr/local/bin/gosu.asc && \  
rm -rf /root/.gnupg/ && \  
chmod +x /usr/local/bin/gosu && \  
mkdir -p /agens-graph && \  
chown -Rf agraph /agens-graph  
  
VOLUME ["/agens-graph"]  
  
ADD AgensGraph_v1.3.1_linux.tar.gz /agens-graph/  
  
ENV GOSU_VERSION=1.20 \  
AGDATA=/agens-graph/data \  
PATH=/agens-graph/AgensGraph/bin:$PATH \  
LD_LIBRARY_PATH=/agens-graph/AgensGraph/lib:$LD_LIBRARY_PATH  
  
COPY agens-graph /usr/local/bin/  
COPY docker-entrypoint.sh /  
  
RUN mkdir /docker-entrypoint-initdb.d && \  
chmod +x docker-entrypoint.sh && \  
chmod +x /usr/local/bin/agens-graph  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["agens-graph"]  

