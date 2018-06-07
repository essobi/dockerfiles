FROM greatbsky/centos7  
MAINTAINER architect.bian  
LABEL name="sshcentos7" license="MIT" build-date="20170307"  
  
ENV VERSION 1.0.0  
RUN yum update -y && yum install -y openssh-server openssh-clients  
  
EXPOSE 22  
CMD /usr/sbin/sshd & tail -f /dev/null

