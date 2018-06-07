FROM centos:6  
MAINTAINER FayeHuang  
#  
RUN mkdir /docker_init  
WORKDIR /docker_init  
#  
RUN yum -y update && yum -y upgrade  
RUN yum -y install epel-release  
RUN yum -y install openssh-clients openssh-server \  
vim sudo wget git npm && \  
yum clean all  
  
RUN rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed -i '/pam_loginuid.so/c session optional pam_loginuid.so'
/etc/pam.d/sshd  
RUN mkdir ssh  
COPY ssh_init.sh ssh/ssh_init.sh  
RUN chmod +x ssh/ssh_init.sh  
  
# install wetty  
RUN git clone https://github.com/krishnasrinivas/wetty && cd wetty && npm
install  
# fix root can't login  
COPY app.js wetty/app.js  
  
# fix pkg_resources.DistributionNotFound: meld3>=0.6.5 , update python
setuptools  
# refs : https://github.com/Supervisor/meld3/issues/23  
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python  
RUN easy_install pip && pip install supervisor  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22 3000  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

