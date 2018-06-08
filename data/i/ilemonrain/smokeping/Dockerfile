FROM centos:7.4.1708  
  
LABEL MAINTAINER iLemonrain <ilemonrain@ilemonrain.com>  
  
# 编译环境变量  
ENV SYSTEM_ROOT_PASSWORD=smokeping \  
TZ=Asia/Shanghai \  
SMOKEPING_SMOKEPING_PASSWORD=smokeping  
  
# 安装系统核心更新  
RUN (yum install epel-release -y ;\  
yum update -y ;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# 安装系统基础组件  
RUN (yum install wget tzdata -y ;\  
/bin/cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone ;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# 安装编译组件  
RUN (yum install gcc make -y ;\  
mkdir /source/ ;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# 安装Apache  
RUN (yum install httpd httpd-devel mod_ssl -y)  
  
# 安装OpenSSH-Server  
RUN (yum update -y; \  
yum install -y openssh-server ;\  
sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config; \  
sed -i 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config; \  
sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config; \  
mkdir -p /root/.ssh/; \  
echo "StrictHostKeyChecking=no" > /root/.ssh/config; \  
echo "UserKnownHostsFile=/dev/null" >> /root/.ssh/config; \  
ssh-keygen -A ;\  
echo "root:${SYSTEM_ROOT_PASSWORD}" | chpasswd ;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# 编译安装 fping  
COPY source/fping-4.0.tar.gz /source/fping-4.0.tar.gz  
RUN (cd /source/ ;\  
tar -zxvf fping-4.0.tar.gz ;\  
cd fping-4.0 ;\  
./configure && make && make install ;\  
cd / ;\  
rm -rf /source/fping-4.0/ ;\  
rm -f /source/fping-4.0.tar.gz )  
  
# 编译安装 echoping  
COPY source/echoping-6.0.2.tar.gz /source/echoping-6.0.2.tar.gz  
RUN (yum install -y file popt popt-devel openssl openssl-devel libidn libidn-
devel ;\  
cd /source/ ;\  
tar -zxvf echoping-6.0.2.tar.gz ;\  
cd echoping-6.0.2 ;\  
./configure --prefix=/usr/local/echoping --with-ssl ;\  
make && make install ;\  
cd / ;\  
rm -rf /source/echoping-6.0.2/ ;\  
rm -f /source/echoping-6.0.2.tar.gz;\  
ln -s /usr/local/echoping/bin/echoping /usr/local/sbin/echoping ;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# 编译安装 Smokeping  
COPY source/smokeping-2.7.1.tar.gz /source/smokeping-2.7.1.tar.gz  
RUN (yum install rrdtool perl-rrdtool openssl openssl-devel -y ;\  
yum install perl-Sys-Syslog perl-Module-CoreList perl-ExtUtils-Manifest \  
perl-Digest-MD5 perl-IPC-Cmd -y ;\  
yum install perl-CPAN perl-Sys-Syslog perl-Module-CoreList perl-CGI \  
perl-Digest-MD5 perl-Digest-HMAC perl-Test-NoWarnings \  
perl-Test-Deep perl-Test-Warn perl-CPAN-Meta perl-Module-Build \  
perl-Test-RequiresInternet perl-URI -y;\  
cd /source/ ;\  
tar -zxvf smokeping-2.7.1.tar.gz ;\  
cd smokeping-2.7.1 ;\  
export PERL5LIB=/usr/local/smokeping/thirdparty/lib/perl5/ ;\  
./configure --prefix=/usr/local/smokeping ;\  
gmake && gmake install ;\  
cd / ;\  
rm -rf /source/smokeping-2.7.1 ;\  
rm -f /source/smokeping-2.7.1.tar.gz ;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# Smokeping 配置  
RUN (DOCKER_HOST_IP=$(curl -s whatismyip.akamai.com) \  
yum -y install wqy-zenhei-fonts ;\  
cd /usr/local/smokeping ;\  
mkdir cache data var ;\  
touch /var/log/smokeping.log ;\  
chown apache:apache cache/ data/ var/ /var/log ;\  
cp /usr/local/smokeping/htdocs/smokeping.fcgi.dist
/usr/local/smokeping/htdocs/smokeping.fcgi ;\  
cp /usr/local/smokeping/etc/config.dist /usr/local/smokeping/etc/config ;\  
ln -s /usr/local/sbin/fping /usr/sbin/fping ;\  
sed -i 's#step = 300#step = 60#g' /usr/local/smokeping/etc/config ;\  
sed -i 's#pings = 20#pings = 10#g' /usr/local/smokeping/etc/config ;\  
sed -i "s/sendmail =/#sendmail =/g" /usr/local/smokeping/etc/config ;\  
htpasswd -cb /usr/local/smokeping/htdocs/htpasswd smokeping
${SMOKEPING_SMOKEPING_PASSWORD} ;\  
chmod 600 /usr/local/smokeping/etc/smokeping_secrets.dist ;\  
sed -i "160i \'--font\'\, \"TITLE:20:WenQuanYi Zen Hei Mono\"\,"
/usr/local/smokeping/lib/Smokeping/Graphs.pm ;\  
sed -i "50i charset= utf-8 " /usr/local/smokeping/etc/config ;\  
ln -s /usr/local/smokeping /smokeping ;\  
ln -s /usr/local/smokeping/bin/smokeping /usr/local/sbin/smokeping ;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# Apache 配置  
RUN (echo "Alias /css \"/usr/local/smokeping/htdocs/css/\"" >>
/etc/httpd/conf/httpd.conf ;\  
echo "Alias /js \"/usr/local/smokeping/htdocs/js\"" >>
/etc/httpd/conf/httpd.conf ;\  
echo "Alias /cache \"/usr/local/smokeping/cache/\"" >>
/etc/httpd/conf/httpd.conf ;\  
echo "Alias /cropper \"/usr/local/smokeping/htdocs/cropper/\"" >>
/etc/httpd/conf/httpd.conf ;\  
echo "Alias / \"/usr/local/smokeping/htdocs/smokeping.fcgi\"" >>
/etc/httpd/conf/httpd.conf ;\  
echo "<Directory \"/usr/local/smokeping\">" >> /etc/httpd/conf/httpd.conf ;\  
echo "AllowOverride None" >> /etc/httpd/conf/httpd.conf ;\  
echo "Options All" >> /etc/httpd/conf/httpd.conf ;\  
echo "AddHandler cgi-script .fcgi .cgi" >> /etc/httpd/conf/httpd.conf ;\  
echo "AllowOverride AuthConfig" >> /etc/httpd/conf/httpd.conf ;\  
echo "Order allow,deny" >> /etc/httpd/conf/httpd.conf ;\  
echo "Allow from all" >> /etc/httpd/conf/httpd.conf ;\  
echo "AuthName \"Smokeping\"" >> /etc/httpd/conf/httpd.conf ;\  
echo "AuthType Basic" >> /etc/httpd/conf/httpd.conf ;\  
echo "AuthUserFile /usr/local/smokeping/htdocs/htpasswd" >>
/etc/httpd/conf/httpd.conf ;\  
echo "Require valid-user" >> /etc/httpd/conf/httpd.conf ;\  
echo "DirectoryIndex smokeping.fcgi" >> /etc/httpd/conf/httpd.conf;\  
echo "</Directory>" >> /etc/httpd/conf/httpd.conf )  
  
# 添加启动脚本  
ADD scripts/entrypoint.sh /usr/local/sbin/entrypoint.sh  
  
# 持久化存储  
VOLUME [ "/smokeping" ]  
  
# 开放端口  
EXPOSE 22 80 443  
  
# 启动命令行  
CMD [ "sh", "/usr/local/sbin/entrypoint.sh" ]

