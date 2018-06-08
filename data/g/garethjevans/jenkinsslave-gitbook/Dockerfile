FROM garethjevans/jenkinsslave-ubuntu:v2.0-pre2  
  
ENV NODE_FLAVOUR=6.x  
  
USER root  
  
RUN curl -L https://github.com/opencontrol/compliance-
masonry/releases/download/v1.1.2/compliance-masonry_1.1.2_linux_amd64.tar.gz
-o compliance-masonry.tar.gz && \  
tar -xf compliance-masonry.tar.gz && \  
cp compliance-masonry_1.1.2_linux_amd64/compliance-masonry /usr/local/bin  
  
RUN curl -sL https://deb.nodesource.com/setup_${NODE_FLAVOUR} | bash - && \  
apt-get update && \  
apt-get -y install nodejs calibre python-pip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install gitbook-cli gitbook-plugin-simple-page-toc -g  
  
RUN pip install -U mkdocs mkdocs-windmill  
  
USER jenkins  
  
RUN gitbook --version  

