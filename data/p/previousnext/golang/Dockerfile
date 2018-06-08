FROM ubuntu:14.04  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
ENV GOBALL go1.4.1.linux-amd64.tar.gz  
  
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
  
# Golang.  
RUN cd /tmp && wget -q https://storage.googleapis.com/golang/$GOBALL  
RUN cd /tmp && tar -C /usr/local -xzf $GOBALL  
RUN mkdir -p /opt/golang  
RUN rm /tmp/$GOBALL  
  
# ENV.  
RUN echo GOPATH=/opt/golang >> /etc/environment  
RUN echo GOPATH=/opt/golang >> /etc/profile  
RUN echo PATH=$PATH:/usr/local/go/bin:/opt/golang/bin >> /etc/environment  
RUN echo PATH=$PATH:/usr/local/go/bin:/opt/golang/bin >> /etc/profile  
  
CMD /usr/sbin/sshd -D  

