FROM buildpack-deps:jessie-scm  
  
# 签名  
MAINTAINER saymagic "zhuxiaole@zhuxiaole.org"  
# gcc for cgo  
RUN apt-get update && apt-get install -y --no-install-recommends \  
sudo \  
g++ \  
gcc \  
libc6-dev \  
make \  
pkg-config \  
&& rm -rf /var/lib/apt/lists/*  
  
#安装ssh服务  
# Install packages  
RUN apt-get update && apt-get -y install openssh-server pwgen && \  
mkdir -p /var/run/sshd && \  
sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config && \  
sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/g"
/etc/ssh/sshd_config  
  
ADD set_ssh_pw.sh /set_ssh_pw.sh  
ADD run.sh /run.sh  
ADD IntelliJIDEALicenseServer_linux_amd64
/IntelliJIDEALicenseServer_linux_amd64  
ADD IntelliJIDEALicenseServer.html /IntelliJIDEALicenseServer.html  
RUN chmod a+x /*.sh  
RUN chmod a+x /IntelliJIDEALicenseServer_linux_amd64  
  
ENV AUTHORIZED_KEYS **None**  
ENV SSH_USER ssh_user  
  
#安装相关工具  
RUN apt-get update && apt-get install net-tools  
RUN apt-get update && apt-get install vim -y  
  
ENV IDEA_USER_NAME idea_user  
ENV IDEA_SERVER_PORT 10818  
ENV PRO_LONGATION_PERIOD 3600000  
EXPOSE 22  
EXPOSE $IDEA_SERVER_PORT  
  
CMD ["/run.sh"]  

