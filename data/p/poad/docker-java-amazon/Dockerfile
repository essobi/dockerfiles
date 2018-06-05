FROM amazonlinux:2016.09  
MAINTAINER PoaD  
  
USER root  
  
RUN yum -y install yum-plugin-fastestmirror  
  
RUN yum -y install vim passwd openssh sudo iproute curl which tar sudo
openssh-server openssh-clients rsync java-1.8.0-openjdk java-1.8.0-openjdk-
devel; \  
yum update -y libselinux  
RUN rm -rf /var/cache/yum/* && \  
yum clean all  
  
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  

