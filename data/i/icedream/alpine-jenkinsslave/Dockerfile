FROM alpine:latest  
MAINTAINER Carl Kittelberger, icedream@icedream.pw  
  
  
# install all packages  
RUN \  
apk add --no-cache \  
autoconf \  
automake \  
alpine-sdk \  
ca-certificates \  
coreutils \  
curl \  
cvs \  
git \  
openjdk7-jre-base \  
mercurial \  
openssh \  
subversion \  
sudo \  
tar \  
unzip \  
wget \  
xz \  
zip \  
&&\  
update-ca-certificates >/dev/null 2>&1  
# prepare the jenkins user  
RUN adduser -g "Jenkins slave user" -s /bin/sh -D jenkins && \  
passwd -d jenkins && \  
mkdir -p /tmp && \  
chmod 777 /tmp && \  
mkdir ~jenkins/.ssh && \  
chown jenkins:jenkins ~jenkins/.ssh && \  
chmod 700 ~jenkins/.ssh  
  
# passwordless sudo for extra package installations, etc.  
RUN echo '' >> /etc/sudoers && \  
echo 'jenkins ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
# clean up  
RUN rm -rf /tmp/* /var/tmp/* /etc/ssh/ssh_host_*  
  
# ssh preparation  
RUN mkdir -p /var/run/sshd  
  
COPY start.sh /  
RUN chmod +x /start.sh  
CMD ["/start.sh"]  
  
# SSH for Jenkins master  
EXPOSE 22  

