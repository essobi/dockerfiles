FROM ubuntu:12.04  
MAINTAINER Yale Huang <yale.huang@trantect.com>  
  
RUN apt-get install -y curl  
RUN curl http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -  
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >>
/etc/apt/sources.list  
RUN echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list  
RUN apt-get update  
# HACK: https://issues.jenkins-ci.org/browse/JENKINS-20407  
RUN mkdir /var/run/jenkins  
RUN apt-get install -y jenkins=1.561 openssh-server supervisor  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
RUN echo 'root:root' | chpasswd  
ADD run /usr/local/bin/  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
EXPOSE 22 8080  
VOLUME ["/var/lib/jenkins"]  
CMD ["/usr/bin/supervisord"]  

