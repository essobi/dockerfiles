FROM centos:latest  
  
RUN yum -y update && yum -y install epel-release && \  
yum -y install jq wget nodejs bzip2 curl net-tools fontconfig freetype
freetype-devel fontconfig-devel libyaml-devel libpcap-devel libstdc++ ethtool
pcre tcpdump pcre-devel libyaml pkgconfig flex bison gcc-c++ zlib-devel
e2fsprogs-devel openssl-devel file-devel make gettext libuuid-devel perl-JSON
bzip2-libs bzip2-devel perl-libwww-perl libpng-devel xz libffi-devel GeoIP vim
&& \  
wget https://files.molo.ch/builds/centos-7/moloch-1.1.1-1.x86_64.rpm && \  
rpm -i moloch-1.1.1-1.x86_64.rpm  
  
ADD scripts /data/moloch/  
  
ENV ES_HOST=elasticsearch \  
NETWORK_INTERFACE=eth0 \  
CLUSTER_PW=secretpw \  
ADMIN_PW=supersecretpw \  
# true or false, both cannot be set to false  
SENSOR=true \  
VIEWER=true  
  
RUN chmod +x /data/moloch/*.sh && \  
chmod +x /data/moloch/db/db.pl /data/moloch/*/*.sh && \  
/data/moloch/configmoloch.sh && \  
cd /data/moloch/viewer && \  
ln -s /data/moloch/bin/node /usr/bin/nodejs && \  
/data/moloch/bin/npm update && \  
npm install . && \  
yum clean -y all  
  
ADD etc/config.ini /data/moloch/etc/config.ini  
RUN chmod 755 /data/moloch/etc/config.ini  
  
EXPOSE 8005  
  
WORKDIR /data/moloch  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  

