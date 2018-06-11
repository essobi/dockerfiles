FROM jenkins  
  
USER root  
  
RUN apt-get update -qq && apt-get install -qqy \  
sudo \  
apparmor \  
mercurial \  
apt-transport-https \  
ca-certificates \  
curl \  
iptables \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
RUN usermod -a -G docker jenkins  
  
VOLUME /var/lib/docker  
  
COPY startup.sh /  
  
CMD /startup.sh  

