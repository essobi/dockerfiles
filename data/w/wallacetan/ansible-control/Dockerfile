FROM centos:latest  
  
RUN yum clean all && \  
yum -y install epel-release && \  
yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-
paramiko python-setuptools python2-pip && \  
yum -y install git vim wget tree openssh-client jq traceroute openvpn && \  
yum -y install net-tools bind-utils  
  
ADD requirements.txt .  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
  
#RUN echo -e '[local]\nlocalhost' > /etc/ansible/hosts  
RUN useradd ansible && \  
mkdir /home/ansible/.ssh && \  
chown ansible:ansible /home/ansible/.ssh  
  
ADD VERSION .  
  
ENV ANSIBLE_VERSION 2.5.3  
ENV TZ=Asia/Singapore  
  
# tail is running in the foreground to keep container running  
CMD ["tail", "-f", "/dev/null"]  

