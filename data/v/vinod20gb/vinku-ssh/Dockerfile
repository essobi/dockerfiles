FROM node:6.2.2  
MAINTAINER Azure App Services Container Images <appsvc-images@microsoft.com>  
  
COPY startup /opt/startup  
COPY sshd_config /etc/ssh/  
  
RUN echo "root:Docker!" | chpasswd \  
&& echo "cd /home" >> /etc/bash.bashrc \  
&& apt-get update \  
&& apt install -y --no-install-recommends openssh-server vim curl wget
tcptraceroute \  
&& chmod 755 /opt/startup/init_container.sh \  
&& cd /opt/startup \  
&& npm install  
  
ENV PORT 8080  
EXPOSE 2222 80  
ENV PATH ${PATH}:/home/site/wwwroot  
  
WORKDIR /home/site/wwwroot  
  
ENTRYPOINT ["/opt/startup/init_container.sh"]  
  

