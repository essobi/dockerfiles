# base image  
FROM centos:centos6  
  
MAINTAINER shufo  
  
# Install Packages  
RUN yum update -y  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum install -y passwd openssh openssh-server openssh-clients sudo python-
pip  
  
# Install supervisor  
RUN pip install supervisor  
RUN mkdir /var/log/supervisor  
ADD templates/supervisord.conf /etc/supervisord.conf  
RUN mkdir /etc/supervisord.d  
  
## Set up SSH  
RUN mkdir /var/log/ssh  
ADD authorized_keys /root/.ssh/authorized_keys  
RUN chmod 700 /root/.ssh && chmod 600 /root/.ssh/authorized_keys  
ADD templates/sshd.conf /etc/supervisord.d/sshd.conf  
  
## Set up SSH Host Key  
RUN /usr/bin/ssh-keygen -q -t rsa1 -f /etc/ssh/ssh_host_key -C '' -N ''  
RUN chmod 600 /etc/ssh/ssh_host_key && chmod 644 /etc/ssh/ssh_host_key.pub  
RUN /usr/bin/ssh-keygen -q -t rsa -f /etc/ssh/ssh_host_rsa_key -C '' -N ''  
RUN chmod 600 /etc/ssh/ssh_host_rsa_key && chmod 644
/etc/ssh/ssh_host_rsa_key.pub  
RUN /usr/bin/ssh-keygen -q -t dsa -f /etc/ssh/ssh_host_dsa_key -C '' -N ''  
RUN chmod 600 /etc/ssh/ssh_host_dsa_key && chmod 644
/etc/ssh/ssh_host_dsa_key.pub  
  
## Set up SSHD config  
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
# set root password to `root`  
RUN echo "root" > /root/password  
RUN bash -c 'echo "root:root" | chpasswd'  
  
# RUN supervisor  
CMD ["/usr/bin/supervisord", "-n"]  

