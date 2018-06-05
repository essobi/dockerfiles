# How to execute:  
# $ docker build -t fiware-aiakos .  
# $ docker run -p 3001:3001 -d fiware-aiakos  
FROM centos:7  
ADD fiware.repo /etc/yum.repos.d/fiware.repo  
RUN curl --silent --location https://rpm.nodesource.com/setup_4.x | bash -  
RUN yum install -y gcc-c++ make  
RUN yum install -y sudo  
RUN yum -y install git nodejs rpm-build initscripts crontabs  
RUN yum -y install fiware-aiakos  
WORKDIR /opt/fiware/fiware-aiakos  
COPY aiakos.yml /etc/sysconfig/fiware-aiakos.yml  
EXPOSE 3001  
VOLUME /sys/fs/cgroup /run /tmp  
ENV container=docke  
COPY start.sh start.sh  
CMD ./start.sh  
  

