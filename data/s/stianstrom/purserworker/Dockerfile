# sshd  
#  
# VERSION 0.0.2  
FROM ubuntu:14.04  
MAINTAINER Stian Strom Anderssen <s177437@stud.hioa.no>  
  
ENV TERM xterm  
RUN apt-get update && apt-get install -y openssh-server python-pip git git-
core httperf libwww-perl  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN pip install pika==0.9.8  
RUN pip install httplib2  
RUN pip install beautifulsoup  
RUN mkdir -p /root/.ssh/  
ADD id_rsa /root/.ssh/id_rsa  
RUN chmod 700 /root/.ssh/id_rsa  
RUN touch /root/.ssh/known_hosts  
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config  
# SSH login fix. Otherwise user is kicked off after login  
RUN cd /root && git clone git@github.com:s177437/uptime_challenge_master.git  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
ADD ./startup.sh /opt/startup.sh  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
CMD ["/bin/bash", "/opt/startup.sh"]  
  

