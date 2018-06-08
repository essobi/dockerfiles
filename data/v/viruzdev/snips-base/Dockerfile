FROM debian:jessie-slim  
MAINTAINER Pascal Mattes <pascal.mattes@icloud.com>  
  
#Dependencies  
RUN apt-get update && apt-get install -y apt-transport-https wget git dirmngr
python-pip python-sklearn python-dev bzip2 supervisor init-system-helpers  
  
#Add Snips Repo  
RUN echo "deb https://debian.snips.ai/jessie stable main" >
/etc/apt/sources.list.d/snips.list ; apt-key adv --keyserver pgp.surfnet.nl
--recv-keys F727C778CCB0A455  
  
#Install Snips  
RUN apt-get update && apt-get install -y snips-platform-voice  

