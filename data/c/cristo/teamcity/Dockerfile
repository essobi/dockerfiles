FROM ubuntu:14.04.4  
MAINTAINER Olexander Kutsenko <olexander.kutsenko@gmail.com>  
  
#Install Dependencies  
RUN apt-get update  
RUN apt-get install -y software-properties-common python-software-properties  
RUN apt-get install -y git git-core vim nano mc nginx tmux curl unzip wget  
  
# SSH service  
RUN apt-get update  
RUN apt-get install -y openssh-server openssh-client  
RUN apt-get install -y python-software-properties  
RUN sudo mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
#change 'pass' to your secret password  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#Install Percona Mysql 5.6 server  
RUN wget https://repo.percona.com/apt/percona-release_0.1-3.$(lsb_release
-sc)_all.deb  
RUN dpkg -i percona-release_0.1-3.$(lsb_release -sc)_all.deb  
RUN rm percona-release_0.1-3.$(lsb_release -sc)_all.deb  
RUN apt-get update  
RUN echo "percona-server-server-5.6 percona-server-server/root_password
password root" | sudo debconf-set-selections  
RUN echo "percona-server-server-5.6 percona-server-server/root_password_again
password root" | sudo debconf-set-selections  
RUN apt-get install -y percona-server-server-5.6  
COPY configs/mysql/my.cnf /etc/mysql/my.cnf  
  
#Install Java 8  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
# Accept license non-iteractive  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
RUN apt-get install -y oracle-java8-set-default  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" | sudo tee -a /etc/environment  
RUN export JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
#install TeamCity  
RUN apt-get update  
RUN wget https://download.jetbrains.com/teamcity/TeamCity-10.0.2.tar.gz  
RUN tar -xvzf TeamCity-*  
RUN mv TeamCity /opt  
  
#Copying configs  
COPY configs/autostart.sh /root/autostart.sh  
COPY configs/bash.bashrc /etc/bash.bashrc  
COPY configs/.bashrc /root/.bashrc  
COPY configs/teamcity /etc/init.d/teamcity  
RUN chmod +x /root/*.sh /etc/init.d/teamcity  
RUN chmod +x /opt/TeamCity/bin/*.sh  
  
#MySQL driver  
RUN mkdir -p /root/.BuildServer/lib/jdbc  
COPY configs/mysql-connector-java-5.1.35-bin.jar /root/.BuildServer/lib/jdbc/  
RUN chmod +x /root/.BuildServer/lib/jdbc/mysql-connector-java-5.1.35-bin.jar  
  
#Install locale  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
#etcKeeper  
RUN mkdir -p /root/etckeeper  
COPY configs/etckeeper.sh /root/etckeeper.sh  
COPY configs/files/etckeeper-hook.sh /root/etckeeper/etckeeper-hook.sh  
RUN chmod +x /root/etckeeper/*.sh  
RUN chmod +x /root/*.sh  
RUN /root/etckeeper.sh  
  
#open ports  
EXPOSE 8111 22 80  

