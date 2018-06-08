FROM protopilotfactory/node:latest  
MAINTAINER Niek Palm <dev.npalm@gmail.com>  
  
RUN curl -SL
"https://cli.run.pivotal.io/stable?release=debian64&version=6.16.1&source=github-
rel" > cf-cli.deb \  
&& dpkg -i cf-cli.deb \  
&& rm -rf /tmp/cf-cli.deb  
  
RUN apt-get update \  
&& apt-get install apache2-utils -y  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

