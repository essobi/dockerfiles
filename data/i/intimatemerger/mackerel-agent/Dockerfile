FROM centos:7  
ENV DOCKER_VERSION=1.12.1  
COPY repos/ /etc/yum.repos.d/  
  
RUN yum -y install mackerel-agent \  
mackerel-agent-plugins \  
docker-engine-$DOCKER_VERSION && \  
yum clean all  
  
COPY mackerel-agent/ /etc/mackerel-agent/  
COPY startup.sh /startup.sh  
  
ENV TZ=Asia/Tokyo \  
AUTO_RETIREMENT=1  
CMD ["/startup.sh"]  

