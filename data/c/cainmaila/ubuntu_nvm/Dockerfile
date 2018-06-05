FROM ubuntu:16.10  
MAINTAINER docker_user cain@cainplay.com  
RUN apt-get update && apt-get upgrade -y && apt-get install -y git wget &&
apt-get install -y git curl  
ENV NVM_DIR=/root/.nvm  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.31.1/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install 6.9.1 \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y yarn  
CMD ["bash"]  

