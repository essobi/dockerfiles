# Build using: docker build -f Dockerfile.gocd-agent -t gocd-agent .  
FROM phusion/baseimage:0.9.16  
MAINTAINER Aravind SV <arvind.sv@gmail.com>  
  
#ADD gocd-common/sources.list /etc/apt/sources.list  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
RUN apt-get update && apt-get install -y -q unzip oracle-java7-installer git
maven ant  
  
RUN mkdir /etc/service/go-agent  
ADD gocd-agent/go-agent-start.sh /etc/service/go-agent/run  
ADD gocd-agent/autoregister.mvn.properties /var/lib/go-
agent/config/autoregister.properties  
  
ADD http://download.go.cd/gocd-deb/go-agent-15.2.0-2248.deb /tmp/go-agent.deb  
  
WORKDIR /tmp  
RUN dpkg -i /tmp/go-agent.deb  
RUN sed -i 's/DAEMON=Y/DAEMON=N/' /etc/default/go-agent  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/sbin/my_init"]  

