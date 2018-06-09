FROM centos:7  
MAINTAINER Adrian B. Danieli "https://github.com/sickp"  
RUN \  
yum -y install openssh-clients openssh-server && \  
yum -y clean all && \  
yum -y install git && \  
touch /run/utmp && \  
chmod u+s /usr/bin/ping && \  
echo "root:root" | chpasswd  
  
RUN \  
cd ~ && git clone https://github.com/shadowsocksr/shadowsocksr.git  
  
COPY entrypoint.sh /  
  
EXPOSE 22  
EXPOSE 8080  
EXPOSE 9000  
ENTRYPOINT ["/entrypoint.sh"]  

