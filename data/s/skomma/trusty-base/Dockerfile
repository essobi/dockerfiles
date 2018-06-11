FROM ubuntu:trusty  
ENV DEBIAN_FRONTEND noninteractive  
  
MAINTAINER Syunsuke Komma <syunsuke@weseek.co.jp>  
  
  
  
## Fix some issues with APT packages.  
## See https://github.com/dotcloud/docker/issues/1024  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
## Replace the 'ischroot' tool to make it always return true.  
## Prevent initscripts updates from breaking /dev/shm.  
## https://journal.paul.querna.org/articles/2013/10/15/docker-ubuntu-on-
rackspace/  
## https://bugs.launchpad.net/launchpad/+bug/974584  
RUN dpkg-divert --local \--rename --add /usr/bin/ischroot  
RUN ln -sf /bin/true /usr/bin/ischroot  
  
# Configure no init scripts to run on package updates.  
ADD src/policy-rc.d /usr/sbin/policy-rc.d  
  
ADD src/sources.list /etc/apt/  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
## install essential packages  
RUN apt-get install -y --no-install-recommends dialog vim nano psmisc
language-pack-en software-properties-common supervisor  
  
## Fix locale.  
RUN locale-gen en_US  
  
## Fix timezone.  
RUN echo "Asia/Tokyo" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
## sudoers Settings  
RUN cp /etc/sudoers /tmp/sudoers.new && \  
sed -i -e "s/%sudo.*/%sudo ALL=(ALL) NOPASSWD: ALL/g" /tmp/sudoers.new && \  
cp /tmp/sudoers.new /etc/sudoers  
  
## install utilities  
RUN apt-get install -y git tmux openssh-server  
  
## add user  
RUN useradd -d /home/syunsuke -m -s /bin/bash syunsuke && \  
usermod -aG sudo syunsuke  
## add user's authorized_keys  
## MUST install by the below order  
## https://github.com/dotcloud/docker/issues/1295#issuecomment-21651778  
ADD src/authorized_keys /home/syunsuke/.ssh/  
RUN chown -R syunsuke: /home/syunsuke/.ssh && \  
chmod 700 /home/syunsuke/.ssh  
  
## add user(common user)  
RUN useradd -d /home/ubuntu -m -s /bin/bash ubuntu && \  
usermod -aG sudo ubuntu  
RUN echo 'ubuntu:ubuntu' > /tmp/ubuntu.chpasswd  
RUN cat /tmp/ubuntu.chpasswd | chpasswd  
  
## supervisor settings  
ADD src/supervisord.conf /etc/supervisor/conf.d/no-daemon.conf  
ADD src/supervisord-sshd.conf /etc/supervisor/conf.d/sshd.conf  
  
## sshd Settings  
RUN sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional
pam_loginuid.so/g' /etc/pam.d/sshd  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV DEBIAN_FRONTEND dialog  
  
  
# Expose the container's port 22  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  

