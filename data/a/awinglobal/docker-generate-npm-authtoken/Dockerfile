FROM ubuntu:16.04  
MAINTAINER Anojan Sivarajah <anojan.sivarajah@awin.com>  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties sudo curl  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install -yq git expect-dev nodejs  
RUN npm install -g npm n && n 0.12  
ADD bin/ /usr/local/bin  
CMD ["bash", "/usr/local/bin/npm.sh"]  

