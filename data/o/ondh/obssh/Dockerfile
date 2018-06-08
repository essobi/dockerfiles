FROM centos:6  
LABEL maintainer="Tonio"  
  
ARG PACKAGE="wget gcc zlib-devel openssl-devel"  
ARG PACKAGE_TO_CLEAN="cloog-ppl cpp glibc-devel glibc-headers kernel-headers
keyutils-libs-devel krb5-devel libcom_err-devel libgomp libkadm5 libselinux-
devel libsepol-devel mpfr ppl"  
ENV USER_PASSWORD "obssh"  
ENV OBFUSCATE_KEY "yourkeyword"  
COPY start.sh /start.sh  
  
RUN yum install $PACKAGE -y && \  
cd ~ && \  
wget -O ofcssh.tar.gz https://github.com/brl/obfuscated-openssh/tarball/master
&& \  
tar zxvf ofcssh.tar.gz && \  
cd ~/brl-obfuscated-openssh-ca93a2c && \  
./configure && \  
make && \  
echo "sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin" >>
/etc/passwd && \  
make install && \  
useradd obssh && \  
echo obssh:$USER_PASSWORD | chpasswd && \  
rm -rf ~/brl-obfuscated-openssh-ca93a2c && \  
rm -rf ~/ofcssh.tar.gz && \  
yum erase $PACKAGE -y && \  
yum erase $PACKAGE_TO_CLEAN -y && \  
yum clean all && \  
chmod +x /start.sh \  
&& cp /usr/local/etc/sshd_config /usr/local/etc/sshd_config.default \  
&& echo "ObfuscatedPort 22" >> /usr/local/etc/sshd_config \  
&& echo "ObfuscateKeyword $OBFUSCATE_KEY" >> /usr/local/etc/sshd_config  
  
EXPOSE 22  
CMD ["/bin/sh","/start.sh"]

