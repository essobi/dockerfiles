FROM node:4.8.2-slim  
  
RUN DEBIAN_FRONTEND=noninteractive \  
curl http://nginx.org/keys/nginx_signing.key | apt-key add - && \  
echo "deb http://nginx.org/packages/debian/ jessie nginx" | tee
/etc/apt/sources.list.d/nginx.list && \  
echo "deb-src http://nginx.org/packages/debian/ jessie nginx" | tee -a
/etc/apt/sources.list.d/nginx.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian jessie main" | tee
/etc/apt/sources.list.d/mono-official.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
nano \  
jq \  
mono-complete \  
mono-vbnc \  
nginx=1.10.3-1~jessie \  
lsb-release \  
&& wget https://dev.mysql.com/get/mysql-apt-config_0.8.5-1_all.deb && \  
echo "mysql-apt-config mysql-apt-config/select-server select mysql-5.7" |
debconf-set-selections && \  
echo "mysql-apt-config mysql-apt-config/select-tools select Disabled" |
debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive dpkg -i mysql-apt-config_0.8.5-1_all.deb && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
mysql-server && \  
rm -rf /var/lib/apt/lists/* && \  
rm mysql-apt-config_0.8.5-1_all.deb \  
&& wget -q https://dl.minio.io/server/minio/release/linux-
amd64/archive/minio.RELEASE.2017-08-05T00-00-53Z && \  
mv minio.RELEASE.2017-08-05T00-00-53Z /usr/local/bin/minio && \  
chmod +x /usr/local/bin/minio && \  
useradd minio && \  
setcap cap_net_bind_service=+ep /usr/local/bin/minio && \  
mkdir /var/lib/minio && \  
chown minio:minio /var/lib/minio && \  
chmod 750 /var/lib/minio && \  
mkdir /etc/minio && \  
chown minio:minio /etc/minio  
  
COPY ./minio /etc/init.d/minio  
COPY ./mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf  
  
VOLUME /var/lib/mysql  
VOLUME /var/lib/minio

