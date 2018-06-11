# Ubuntu with OpenSSH Server  
  
FROM winggundamth/ubuntu-base:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
# 1) Install OpenSSH and necessary packages  
# 2) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo 'Acquire::http::Proxy "http://172.17.0.1:3142";' \  
> /etc/apt/apt.conf.d/11proxy || true; \  
apt-get update && \  
apt-get install -y openssh-server vim tmux rsync byobu && \  
sed -i 's/required pam_loginuid.so/optional pam_loginuid.so/g' \  
/etc/pam.d/sshd && \  
echo 'export LC_ALL=en_US.UTF-8' > /root/.bash_profile && \  
mkdir -p /var/run/sshd /root/.ssh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /build-files /etc/apt/apt.conf.d/11proxy  
  
CMD ["/usr/sbin/sshd", "-D"]  
EXPOSE 22  
# 1) Prepare authorized_keys file  
RUN mkdir -p /root/.ssh && \  
touch /root/.ssh/authorized_keys && \  
chown -R root:root /root/.ssh && \  
chmod 700 /root/.ssh && \  
chmod 600 /root/.ssh/authorized_keys  

