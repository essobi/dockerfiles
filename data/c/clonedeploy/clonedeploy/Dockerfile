FROM ubuntu:xenial  
  
LABEL maintainer "cdadmin@clonedeploy.org"  
  
ENV DEBIAN_FRONTEND=noninteractive \  
CLONEDEPLOY_VERSION=1.3.2 \  
LOAD_TFTP=true \  
LOAD_SMB=true \  
RW_SMB_PASS=rwpass \  
RO_SMB_PASS=ropass \  
MYSQL_ROOT_PASS=  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian xenial main" | tee
/etc/apt/sources.list.d/mono-xamarin.list  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
libapache2-mod-mono \  
liblz4-tool \  
mono-devel \  
mysql-server \  
samba \  
tftpd-hpa \  
udpcast \  
unzip \  
wget \  
mkisofs \  
&& rm -rf /var/lib/mysql \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -P /tmp
"https://sourceforge.net/projects/clonedeploy/files/Docker/clonedeploy-${CLONEDEPLOY_VERSION}.tar.gz"
\  
&& tar xzf /tmp/clonedeploy-${CLONEDEPLOY_VERSION}.tar.gz -C /usr/src/ \  
&& rm /tmp/clonedeploy-${CLONEDEPLOY_VERSION}.tar.gz  
  
RUN cd /usr/src/clonedeploy \  
&& cp clonedeploy.conf /etc/apache2/sites-available/ \  
&& a2ensite clonedeploy \  
&& mkdir /opt/clonedeploy  
  
RUN { \  
echo '[cd_share]'; \  
echo 'path = /cd_dp'; \  
echo 'valid users = @cdsharewriters, cd_share_ro'; \  
echo 'create mask = 02775'; \  
echo 'directory mask = 02775'; \  
echo 'guest ok = no'; \  
echo 'writable = yes'; \  
echo 'browsable = yes'; \  
echo 'read list = @cdsharewriters, cd_share_ro'; \  
echo 'write list = @cdsharewriters'; \  
echo 'force create mode = 02775'; \  
echo 'force directory mode = 02775'; \  
echo 'force group = +cdsharewriters'; \  
} >> /etc/samba/smb.conf \  
&& addgroup cdsharewriters \  
&& useradd cd_share_ro --shell=/usr/sbin/nologin --no-create-home \  
&& useradd cd_share_rw --shell=/usr/sbin/nologin --no-create-home -G
cdsharewriters \  
&& adduser www-data cdsharewriters  
  
RUN { \  
echo 'TFTP_USERNAME="root"'; \  
echo 'TFTP_DIRECTORY="/tftpboot"'; \  
echo 'TFTP_ADDRESS="0.0.0.0:69"'; \  
echo 'TFTP_OPTIONS="-s -vvvv -m /tftpboot/remap"'; \  
} > /etc/default/tftpd-hpa  
  
EXPOSE 80/tcp \  
137-139/udp \  
9000-10002/udp \  
69/udp \  
445/tcp  
  
VOLUME ["/var/www/html", "/tftpboot", "/cd_dp", "/var/lib/mysql"]  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/bin/bash","/entrypoint.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

