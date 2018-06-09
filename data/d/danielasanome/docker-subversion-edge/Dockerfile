FROM mamohr/centos-java:jre8  
  
MAINTAINER Daniel Rocha Asanome <daniel.asanome@gmail.com>  
  
RUN \  
yum install -y https://$(rpm -E
'%{?centos:centos}%{!?centos:rhel}%{rhel}').iuscommunity.org/ius-release.rpm
&& \  
yum update -y && \  
yum install -y epel-release && \  
yum install -y net-tools python-setuptools hostname inotify-tools yum-utils &&
\  
yum clean all && \  
easy_install supervisor  
  
ENV FILE https://downloads-
guests.open.collab.net/files/documents/61/18759/CollabNetSubversionEdge-5.2.2_linux-x86_64.tar.gz  
  
RUN wget -q ${FILE} -O /tmp/csvn.tgz && \  
mkdir -p /opt/csvn && \  
tar -xzf /tmp/csvn.tgz -C /opt/csvn --strip=1 && \  
rm -rf /tmp/csvn.tgz  
  
ENV RUN_AS_USER collabnet  
  
RUN useradd collabnet && \  
chown -R collabnet.collabnet /opt/csvn && \  
cd /opt/csvn && \  
./bin/csvn install && \  
mkdir -p ./data-initial && \  
cp -r ./data/* ./data-initial && \  
chown root.collabnet /opt/csvn/lib/httpd_bind/httpd_bind && \  
chmod u+s /opt/csvn/lib/httpd_bind/httpd_bind  
  
EXPOSE 3343 4434 18080 80 443  
ADD files /  
  
RUN chmod +x /config/bootstrap.sh  
  
VOLUME /opt/csvn/data  
  
WORKDIR /opt/csvn  
  
ENTRYPOINT ["/config/bootstrap.sh"]  

