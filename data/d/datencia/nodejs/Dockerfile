FROM datencia/base  
  
LABEL maintainer="david.atencia@gmail.com"  
  
ENV NPM_VERSION=5.6.0 \  
YARN_VERSION=1.3.2  
  
RUN echo "Installing basics" && \  
apt-get -qq update && \  
apt-get -qq install -y curl python ca-certificates build-essential --no-
install-recommends && \  
echo "Installing Node.js" && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get -qq update && \  
apt-get -qq install -y nodejs --no-install-recommends && \  
echo "Installing npm & yarn" && \  
npm install -g npm@${NPM_VERSION} yarn@${YARN_VERSION} && \  
echo "Cleaning up" && \  
npm cache clear --force && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  

