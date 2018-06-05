FROM ubuntu:14.04  
MAINTAINER Oleksandr Kutsenko <olexander.kutsenko@gmail.com>  
  
# install Software  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y software-properties-common python-software-properties \  
git git-core vim nano mc unzip wget htop tmux zip  
  
# Install Percona Mysql 5.6 server  
RUN wget https://repo.percona.com/apt/percona-release_0.1-3.$(lsb_release
-sc)_all.deb  
RUN dpkg -i percona-release_0.1-3.$(lsb_release -sc)_all.deb  
RUN rm percona-release_0.1-3.$(lsb_release -sc)_all.deb  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 8507EFA5  
RUN apt-get update  
RUN echo "percona-server-server-5.6 percona-server-server/root_password
password root" | sudo debconf-set-selections  
RUN echo "percona-server-server-5.6 percona-server-server/root_password_again
password root" | sudo debconf-set-selections  
RUN apt-get install -qq -y percona-server-server-5.6  
COPY configs/mysql/my.cnf /etc/mysql/my.cnf  
RUN service mysql start && mysqladmin -uroot -proot create bamboo  
  
# Install SSH service  
RUN sudo apt-get install -y openssh-server openssh-client  
RUN sudo mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
# change 'pass' to your secret password  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# configs bash start  
COPY configs/autostart.sh /root/autostart.sh  
RUN chmod +x /root/autostart.sh  
COPY configs/bash.bashrc /etc/bash.bashrc  
COPY configs/.bashrc /root/.bashrc  
  
# Install locale  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# Install Java 8  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
# Accept license non-iteractive  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer \  
oracle-java8-set-default  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" | sudo tee -a /etc/environment  
RUN export JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
# etcKeeper  
RUN mkdir -p /root/etckeeper  
COPY configs/etckeeper.sh /root/etckeeper.sh  
COPY configs/files/etckeeper-hook.sh /root/etckeeper/etckeeper-hook.sh  
RUN chmod +x /root/etckeeper/*.sh  
RUN chmod +x /root/*.sh  
RUN /root/etckeeper.sh  
RUN rm /etc/apt/sources.list.d/*  
  
# Download and install Bamboo  
RUN cd /opt && wget
https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-5.14.0.2.tar.gz  
RUN cd /opt && tar -xvzf atlassian-bamboo-5.14.0.2.tar.gz  
RUN rm /opt/atlassian-bamboo-5.14.0.2.tar.gz  
RUN echo "bamboo.home=/opt/bamboo-home" > /opt/atlassian-
bamboo-5.14.0.2/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties  
RUN wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.40.tar.gz  
RUN tar -xvzf mysql-connector-java-5.1.40.tar.gz  
RUN rm mysql-connector-java-5.1.40.tar.gz  
RUN mv mysql-connector-java-5.1.40/mysql-connector-java-5.1.40-bin.jar
/opt/atlassian-bamboo-5.14.0.2/lib/  
RUN rm -rf mysql-connector-java-5.1.40  
  
# Open ports: Web, SSH, Bamboo-agent  
EXPOSE 8085 22 54663  
VOLUME ["/opt/bamboo-home"]  
  
CMD /bin/bash

