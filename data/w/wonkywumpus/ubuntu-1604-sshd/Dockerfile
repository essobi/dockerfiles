FROM ubuntu:16.04  
# Install any needed packages specified in requirements.txt  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install libc-dev perl openssl file sudo libdbi-perl
libreadline-dev rsync libsnappy-dev net-tools tzdata libtcl8.6 expect
inetutils-ping dnsutils vim libdbd-mysql-perl libboost-all-dev curl  
RUN apt-get -i install syslog  
RUN apt-get install openssh-server  
  
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

