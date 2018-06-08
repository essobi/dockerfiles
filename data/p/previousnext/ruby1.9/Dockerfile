FROM ubuntu:14.04  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
# APT.  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -fs /bin/true /sbin/initctl  
  
# Tools.  
RUN apt-get install -y make rsync git  
  
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
  
# Ruby.  
RUN apt-get install -y ruby1.9.1-dev  
RUN gem install bundler  
  
CMD /usr/sbin/sshd -D  

