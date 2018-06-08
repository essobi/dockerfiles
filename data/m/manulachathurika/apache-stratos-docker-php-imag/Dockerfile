# ----------------------------------------------------------------------------  
# ----------------------------------------------------------------------------  
  
FROM ubuntu:14.04  
  
RUN apt-get update  
RUN apt-get install -y wget  
  
WORKDIR /opt/  
  
#################################  
# Enable ssh - This is not good. http://jpetazzo.github.io/2014/06/23/docker-
ssh-considered-evil/  
# For experimental purposes only  
##################################  
  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
RUN echo 'root:g' | chpasswd  
RUN sed -i "s/PermitRootLogin without-password/#PermitRootLogin without-
password/" /etc/ssh/sshd_config  
  
##################  
# Install PHP  
##################  
RUN apt-get install -y apache2 php5 zip unzip  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
ADD files/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
##################  
# Install Java  
##################  
ADD packs/jdk-7u7-linux-x64.tar.gz /opt/  
RUN ln -s /opt/jdk1.7.0_07 /opt/java  
  
RUN echo "export JAVA_HOME=/opt/java" >> /root/.bashrc  
RUN echo "export PATH=$PATH:/opt/java/bin" >> /root/.bashrc  
#RUN echo "PATH=$PATH:/opt/java/bin" > /etc/environment  
#ENV JAVA_HOME /opt/java  
#ENV PATH /opt/java/bin:$PATH  
  
##################  
# Configure Agent  
##################  
WORKDIR /mnt/  
  
ADD packs/apache-stratos-cartridge-agent-4.1.0-SNAPSHOT.zip /mnt/apache-
stratos-cartridge-agent-4.1.0-SNAPSHOT.zip  
RUN unzip -q apache-stratos-cartridge-agent-4.1.0-SNAPSHOT.zip  
RUN rm apache-stratos-cartridge-agent-4.1.0-SNAPSHOT.zip  
RUN mv apache-stratos-cartridge-agent* apache-stratos-cartridge-agent  
RUN mkdir -p /mnt/apache-stratos-cartridge-agent/payload  
  
  
#######################  
# ActiveMQ dependencies  
#######################  
ADD packs/activemq/activemq-broker-5.9.1.jar /mnt/apache-stratos-cartridge-
agent/lib/activemq-broker-5.9.1.jar  
ADD packs/activemq/activemq-client-5.9.1.jar /mnt/apache-stratos-cartridge-
agent/lib/activemq-client-5.9.1.jar  
ADD packs/activemq/geronimo-j2ee-management_1.1_spec-1.0.1.jar /mnt/apache-
stratos-cartridge-agent/lib/geronimo-j2ee-management_1.1_spec-1.0.1.jar  
ADD packs/activemq/geronimo-jms_1.1_spec-1.1.1.jar /mnt/apache-stratos-
cartridge-agent/lib/geronimo-jms_1.1_spec-1.1.1.jar  
ADD packs/activemq/hawtbuf-1.9.jar /mnt/apache-stratos-cartridge-
agent/lib/hawtbuf-1.9.jar  
  
EXPOSE 22 80  
  
###################  
# Setup run script  
###################  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
ADD files/populate-user-data.sh /usr/local/bin/populate-user-data.sh  
RUN chmod +x /usr/local/bin/populate-user-data.sh  
  
ENTRYPOINT /usr/local/bin/run | /usr/sbin/sshd -D  

