FROM azul/zulu-openjdk-centos:latest  
MAINTAINER Bard Lind <bard.lind@gmail.com>  
RUN yum install -y yum-cron  
RUN yum -y update  
  
RUN yum install -y wget  
RUN yum install -y unzip  
# Install sshd - should probably be fortified  
RUN yum install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:kjempehemmelig' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN echo "export VISIBLE=now" >> /etc/profile  
RUN /usr/sbin/sshd-keygen  
  
RUN adduser blitz  
  
## Install Apache River  
RUN su - blitz -c "/usr/bin/wget -O apache-river-2.2.2-bin.zip -q -N
http://www.trieuvan.com/apache/river/river-2.2.2/apache-river-2.2.2-bin.zip"  
RUN su - blitz -c "unzip apache-river-2.2.2-bin.zip"  
  
## Install Blitz  
RUN su - blitz -c "/usr/bin/wget -O installer_pj_2_1_7.jar -q -N
https://github.com/downloads/dancres/blitzjavaspaces/installer_pj_2_1_7.jar"  
RUN su - blitz -c "java -Dblitz.nocheck=true -jar installer_pj_2_1_7.jar
/home/blitz/apache-river-2.2.2 /home/blitz/blitz 8085 "  
RUN su - blitz -c "chmod +x ./blitz/*.sh"  
  
## Set up start of services  
RUN yum -y install python-setuptools  
RUN easy_install supervisor  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN ln -s /etc/supervisor/conf.d/supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22 8085 4160  
CMD ["/usr/bin/supervisord"]  

