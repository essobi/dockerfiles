#  
# vim:ts=2:sw=2:et  
#  
FROM fedora:23  
MAINTAINER Rohith <gambol99@gmail.com>  
  
RUN dnf install -y awscli && \  
dnf clean all  
  
ADD run.sh /run.sh  
  
ENTRYPOINT [ "/run.sh" ]  

