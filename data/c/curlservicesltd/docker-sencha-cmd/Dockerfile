FROM openjdk:8-jre  
  
MAINTAINER Mladen Maravic <beb4ch@gmail.com>  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get update && apt-get install -y nodejs \  
&& curl -sS http://cdn.sencha.com/cmd/6.5.3.6/no-jre/SenchaCmd-6.5.3.6-linux-
amd64.sh.zip > /tmp/sencha.zip \  
&& unzip /tmp/sencha.zip -d /tmp \  
&& /tmp/SenchaCmd*.sh -q --all \  
&& rm /tmp/SenchaCmd*.sh  
  
ENTRYPOINT ["/root/bin/Sencha/Cmd/6.5.3.6/sencha"]  
  
WORKDIR /code  

