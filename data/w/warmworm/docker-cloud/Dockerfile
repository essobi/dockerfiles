FROM centos:7  
# install basic tools  
RUN yum install -y epel-release && \  
yum install -y net-tools bind-utils telnet nc wget tcpdump lrzsz  
  
# install openssh and init it  
RUN yum install -y openssh-server openssh-clients python-pip telnet nc &&\  
ssh-keygen -t rsa -N "" -f /etc/ssh/ssh_host_rsa_key &&\  
ssh-keygen -t ecdsa -N "" -f /etc/ssh/ssh_host_ecdsa_key &&\  
ssh-keygen -t ed25519 -N "" -f /etc/ssh/ssh_host_ed25519_key  
  
# install supervisor ctl  
RUN pip install supervisor &&\  
mkdir -p /etc/supervisor.d/conf.d &&\  
echo_supervisord_conf > /etc/supervisor.d/supervisord.conf &&\  
echo "[include]" >> /etc/supervisor.d/supervisord.conf &&\  
echo "files=conf.d/*.ini" >> /etc/supervisor.d/supervisord.conf  
COPY ./sshd.ini /etc/supervisor.d/conf.d/  
  
# install tomcat 8.5.29  
RUN yum install -y java-1.8.0-openjdk  
RUN cd /opt &&\  
wget http://mirrors.hust.edu.cn/apache/tomcat/tomcat-8/v8.5.29/bin/apache-
tomcat-8.5.29.tar.gz &&\  
tar xvzf apache-tomcat-8.5.29.tar.gz &&\  
ln -s /opt/apache-tomcat-8.5.29 tomcat  
  
# expose ssh port  
EXPOSE 22  
# expose tomcat port  
EXPOSE 8080  
EXPOSE 8009  
EXPOSE 8005  
# modify default root passwd  
RUN echo "123456" | passwd --stdin root  
  
# clear yum cache  
RUN yum clean all  
  
CMD ["sh", "-c", "/usr/bin/supervisord -n -c
/etc/supervisor.d/supervisord.conf"]  

