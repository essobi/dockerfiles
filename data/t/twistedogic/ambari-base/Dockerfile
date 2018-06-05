FROM centos:6  
MAINTAINER Jordan Li  
RUN yum update -y  
RUN yum install -y sudo tar wget java-1.7.0-openjdk  
RUN \  
echo "# Install OpenSSH Server" ;\  
yum -y install openssh-server openssh-clients;\  
mkdir -p /var/run/sshd ;\  
echo 'root:passw0rd' | chpasswd ;\  
\  
true  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
RUN sed -i "/^[^#]*UsePAM/ s/.*/#&/" /etc/ssh/sshd_config  
RUN echo "UsePAM no" >> /etc/ssh/sshd_config  
  
RUN wget -nv http://public-
repo-1.hortonworks.com/ambari/centos6/2.x/updates/2.0.0/ambari.repo -O
/etc/yum.repos.d/ambari.repo  
RUN yum update -y  
RUN yum -y install python-setuptools python-meld3 && yum clean all  
RUN easy_install pip && pip install supervisor  
RUN pip install distribute --upgrade  
CMD /usr/sbin/sshd -D  
EXPOSE 8080 22  

