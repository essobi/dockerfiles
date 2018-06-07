FROM ubuntu:14.04  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
# APT.  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -fs /bin/true /sbin/initctl  
  
# Tools.  
RUN apt-get install -y make rsync git curl  
  
# SSHD.  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /root/.ssh  
  
# Root user access.  
ADD authorized_keys /root/.ssh/authorized_keys  
RUN chmod 400 /root/.ssh/authorized_keys  
RUN chown root:root -R /root/.ssh  
  
# Non root user access.  
RUN useradd -ms /bin/bash pnx  
ADD pnx_authorized_keys /home/pnx/.ssh/authorized_keys  
RUN chmod 400 /home/pnx/.ssh/authorized_keys  
RUN chown pnx:pnx -R /home/pnx/.ssh  
# This is common build dir.  
RUN mkdir /data && chown -R pnx:pnx /data  
  
# Packer.  
RUN mkdir /tmp/packer \  
&& cd /tmp/packer \  
&& apt-get update && apt-get install -y curl ca-certificates git unzip --no-
install-recommends && rm -rf /var/lib/apt/lists/* \  
&& curl -O -sS -L
https://dl.bintray.com/mitchellh/packer/packer_0.8.1_linux_amd64.zip \  
&& unzip packer_0.8.1_linux_amd64.zip \  
&& apt-get purge -y --auto-remove curl unzip \  
&& mv packer* /usr/local/bin \  
&& rm -rf /tmp/packer  
  
CMD /usr/sbin/sshd -D  

