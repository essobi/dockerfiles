FROM amazonlinux  
  
RUN yum update -y && yum install -y findutils git which  
  
COPY ./scripts /scripts  
  
ARG vips_version_minimum=8.4.6  
ARG vips_version_latest_major_minor=8.4  
ARG vips_version_latest_patch=6  
RUN sh /scripts/install-vips  
  
ARG node_version=6.1  
ENV NODE_VERSION=$node_version  
  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash &&
\  
source $HOME/.nvm/nvm.sh && \  
nvm install ${node_version} && \  
ln -s "`which node`" /usr/bin/ && \  
ln -s "`which npm`" /usr/bin/  

