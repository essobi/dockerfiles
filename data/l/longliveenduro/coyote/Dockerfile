FROM debian  
  
ADD https://github.com/Landoop/coyote/releases/download/v1.2/coyote-1.2-linux-
amd64 /usr/local/bin  
  
RUN chmod 755 /usr/local/bin/coyote-1.2-linux-amd64  
  
RUN apt-get update && apt-get -y install curl apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common  
  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian $(lsb_release -cs) stable"  
  
RUN apt-get update && apt-get -y install docker-ce  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.14.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
  
RUN chmod +x /usr/local/bin/docker-compose  
  
VOLUME /integrationtests  
  
WORKDIR /integrationtests  
  
ENTRYPOINT ["coyote-1.2-linux-amd64"]  

