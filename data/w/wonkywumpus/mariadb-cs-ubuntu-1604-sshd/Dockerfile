FROM ubuntu:16.04  
# Install any needed packages specified in requirements.txt  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install perl  
RUN apt-get -y install openssl  
RUN apt-get -y install file  
RUN apt-get -y install sudo  
RUN apt-get -y install libdbi-perl  
RUN apt-get -y install libreadline-dev  
RUN apt-get -y install rsync  
RUN apt-get -y install libsnappy-dev  
RUN apt-get -y install net-tools  
RUN apt-get -y install tzdata  
RUN apt-get -y install libtcl8.6  
RUN apt-get -y install expect  
RUN apt-get -y install inetutils-ping  
RUN apt-get -y install dnsutils  
RUN apt-get -y install vim  
RUN apt-get -y install syslog-ng  
RUN apt-get -y install libdbd-mysql-perl  
RUN apt-get -y install libboost-all-dev  
RUN apt-get -y install curl  
  
RUN apt-get -y install openssh-server  
  
RUN curl -o /root/mariadb-columnstore-1.0.10-1-xenial.x86_64.deb.tar.gz
https://downloads.mariadb.com/ColumnStore/1.0.10/ubuntu/dists/xenial/main/binary_amd64/mariadb-
columnstore-1.0.10-1-xenial.x86_64.deb.tar.gz  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:m18#MDB' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

