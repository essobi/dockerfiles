FROM centos:centos6  
MAINTAINER Imagine Chiu<imagine10255@gmail.com>  
  
  
ENV SSH_ROOT_PASSWORD=P@ssw0rd  
  
  
# Install SSH Service  
RUN yum install -y openssh-server passwd  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \  
echo "${SSH_ROOT_PASSWORD}" | passwd "root" \--stdin  
  
# Install MariaDB  
RUN echo -e "[mariadb]" >> /etc/yum.repos.d/MariaDB.repo && \  
echo -e "name = MariaDB" >> /etc/yum.repos.d/MariaDB.repo && \  
echo -e "baseurl = http://yum.mariadb.org/10.0/centos6-amd64" >>
/etc/yum.repos.d/MariaDB.repo && \  
echo -e "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB" >>
/etc/yum.repos.d/MariaDB.repo && \  
echo -e "gpgcheck=1" >> /etc/yum.repos.d/MariaDB.repo && \  
yum -y install MariaDB-Galera-server MariaDB-client galera  
  
# Copy files for setting  
ADD ./docker /opt/  
  
# Create Base Enter Cont Command  
RUN chmod 755 /opt/bash/init-bashrc.sh && echo "/opt/bash/init-bashrc.sh" >>
/root/.bashrc  
  
# Setting DateTime Zone  
RUN cp -p /usr/share/zoneinfo/Asia/Taipei /etc/localtime  
  
# Private expose  
EXPOSE 3306 22  
# Volume for web server install  
VOLUME ["/home/mysql","/home/tmp"]  
  
# Start run shell  
CMD ["bash"]  

