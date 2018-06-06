FROM ppanyukov/vsts-agent-auto:centos7-2.107.1  
# We will run as root and then su to vsoagent to secure  
# env vars etc.  
USER root  
  
COPY files/home/vsoagent/* /home/vsoagent/  
COPY files/etc/yum.repos.d/* /etc/yum.repos.d/  
  
# Install docker client so we can use it even if we  
# run on non-centos hosts (e.g ubuntu).  
# Simply mapping the docker executable from host does not  
# work anymore because of shared libs dependencies which may  
# differ between distributions.  
RUN set -x \  
&& yum -y install \  
docker-engine \  
&& yum clean all  
  
CMD ["/bin/bash", "./run-vsts-agent-d.sh"]  

