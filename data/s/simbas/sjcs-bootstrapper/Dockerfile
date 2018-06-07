FROM debian:testing  
  
WORKDIR /usr/local/bootstrapper/  
  
RUN apt update && apt install --yes curl unzip ca-certificates shellcheck  
RUN curl -L -s
https://github.com/ericchiang/pup/releases/download/v0.4.0/pup_v0.4.0_linux_amd64.zip
-o pup.zip  
RUN unzip pup.zip -d /usr/local/bin/  
ADD . .  
RUN shellcheck *.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  

