FROM centos:centos7  
  
RUN yum-config-manager --add-repo
https://yum.dockerproject.org/repo/main/centos/7 && \  
rpm --import https://yum.dockerproject.org/gpg && \  
yum install -y docker-engine epel-release && \  
yum install -y jq && \  
yum clean all -y  
  
ENV SOURCE_TAG sourcetag:latest  
ENV TARGET_TAG targettag:latest  
ENV TAG_ONLY false  
ENV FORCE_TAG false  
ENV DEBUG_ME false  
  
# Need to be root to access docker.sock  
USER root  
  
ENV HOME /root  
  
COPY "docker-tag-promote.sh" "/usr/local/bin/docker-tag-promote.sh"  
RUN chmod +x /usr/local/bin/docker-tag-promote.sh  
CMD "/usr/local/bin/docker-tag-promote.sh"  

