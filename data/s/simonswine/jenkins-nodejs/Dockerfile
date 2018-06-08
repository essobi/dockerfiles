FROM simonswine/jenkins-debian:wheezy  
MAINTAINER Christian Simon <simon@swine.de>  
# Install man-db  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y man-db  
# Install Nodejs Version Mananger  
RUN su -l -c "touch /jenkins/.profile && curl
https://raw.github.com/creationix/nvm/master/install.sh | sh" jenkins  
# Install Node 0.8  
RUN su -l -c "nvm install 0.8" jenkins  
# Install Node 0.10  
RUN su -l -c "nvm install 0.10" jenkins  
# Default nodejs 0.10  
RUN su -l -c "nvm alias default 0.10" jenkins  

