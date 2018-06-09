#########################################  
# Name: redhab1/centos7-base-ci-jenkins-slave-supervisor  
# Description: Centos7 based Continuous Integration Jenkins Slave image with
Supervisor  
#  
# - Adds:  
# - Supervisor  
#  
# To build image:  
# docker build -t redhab1/centos7-base-ci-jenkins-slave-supervisor .  
#  
# To run container:  
# docker run -d -t -i -p 2222:22 redhab1/centos7-base-ci-jenkins-slave-
supervisor  
#  
# Change Log:  
# 03/18/17: Initial version  
#########################################  
FROM redhab1/centos7-base-ci-jenkins-slave  
  
LABEL name="redhab1/centos7-base-ci-jenkins-slave-supervisor"  
LABEL description="Centos7 based Continuous Integration Jenkins Slave image
with Supervisor"  
LABEL maintainer="Redha Boukefoussa redhab@gmail.com"  
  
RUN echo "Install python-setuptools" \  
&& yum install -y python-setuptools \  
\  
&& echo "Install Supervisor" \  
&& easy_install supervisor \  
&& mkdir -p /etc/supervisor \  
\  
&& echo "Configure Supervisor" \  
&& echo -e "\n\  
[supervisord] \n\  
nodaemon=true \n\  
\n\  
[program:sshd] \n\  
command=/usr/sbin/sshd -D \n\  
priority=1 \n\  
" > /etc/supervisor/supervisord.conf \  
\  
&& echo "Clean up" \  
&& yum clean all \  
&& rm -rf \  
/tmp/* \  
/var/tmp/*  
  
# Standard SSH port  
EXPOSE 22  
  
CMD ["/usr/bin/supervisord"]

