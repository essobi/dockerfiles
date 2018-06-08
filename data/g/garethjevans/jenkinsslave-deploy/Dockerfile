FROM garethjevans/jenkinsslave-ubuntu:v2.0-pre2  
  
ENV CFCLI https://cli.run.pivotal.io/stable?release=debian64&source=github  
  
USER root  
  
RUN wget --quiet ${CFCLI} -O /tmp/cf-cli_amd64.deb && \  
dpkg -i /tmp/cf-cli_amd64.deb && \  
rm /tmp/cf-cli_amd64.deb  
  
  
RUN chown jenkins:jenkins -R /home/jenkins  
  
USER jenkins  
WORKDIR /home/jenkins  

