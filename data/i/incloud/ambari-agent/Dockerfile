FROM jiadx/java-docker:1.8  
ENV PATH=$JAVA_HOME/bin:$PATH  
#--------------local ambari repo  
#ADD repo/ambari_local.repo /etc/yum.repos.d/  
ADD repo/ambari_origin.repo /etc/yum.repos.d/  
  
#-------------install ambari  
RUN yum -y install ntp ambari-agent  
  
#-----------install docker-gen  
RUN yum install -y dnsmasq openssl tar wget  
ENV DOCKER_HOST unix:///var/run/docker.sock  
  
RUN wget -qO- https://github.com/jwilder/docker-
gen/releases/download/0.7.0/docker-gen-linux-amd64-0.7.0.tar.gz | tar xvz -C
/usr/local/bin  
COPY etc-hosts.tmpl /etc/etc-hosts.tmpl  
  
#clean yum cache  
RUN yum clean all  
  
COPY *.sh /  
RUN chmod +x /*.sh  
CMD ["/start-agent.sh"]  
  
WORKDIR /  

