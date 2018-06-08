FROM ubuntu-oracle-jdk8  
MAINTAINER Koert Zeilstra <koert.zeilstra@zencode.nl>  
  
# Build image  
# docker build -t koert/glassfish-4.1 .  
RUN apt-get update && \  
apt-get install -y wget unzip pwgen expect && \  
wget http://download.java.net/glassfish/4.1/release/glassfish-4.1.zip && \  
unzip glassfish-4.1.zip -d /opt && \  
rm glassfish-4.1.zip  
  
ENV PATH /opt/glassfish4/bin:/opt/app/bin:$PATH  
  
RUN mkdir -p /opt/app/bin  
RUN mkdir -p /opt/app/deploy  
  
ADD bin/change_admin_password.sh /opt/app/bin/change_admin_password.sh  
ADD bin/change_admin_password_func.sh
/opt/app/bin/change_admin_password_func.sh  
ADD bin/enable_secure_admin.sh /opt/app/bin/enable_secure_admin.sh  
ADD bin/initialize-glassfish.sh /opt/app/bin/initialize-glassfish.sh  
ADD bin/configure-glassfish.sh /opt/app/bin/configure-glassfish.sh  
RUN chmod +x /opt/app/bin/*.sh  
  
RUN /opt/app/bin/initialize-glassfish.sh  
  
RUN echo 'root:root' | chpasswd  
  
RUN mkdir /etc/service/glassfish  
ADD bin/start-glassfish.sh /etc/service/glassfish/run  
RUN chmod +x /etc/service/glassfish/run  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# 4848 (administration), 8080 (HTTP listener), 8181 (HTTPS listener), 9009
(JPDA debug port)  
EXPOSE 4848 8080 8181 9009  
# CMD ["/opt/app/bin/start-glassfish.sh"]  

