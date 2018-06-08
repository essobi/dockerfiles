# Google mirrors are very fast.  
FROM ozzyjohnson/wheezy-cloudtools  
  
MAINTAINER Ozzy Johnson <ozzy.johnson@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update and install minimal.  
RUN \  
apt-get update \  
\--quiet && \  
apt-get install \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
curl \  
git-core && \  
  
# Clean up packages.  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Fabric to support Sendak.  
RUN pip install \  
fabric  
  
# Node to support Sendak.  
# Taken from: https://github.com/docker-
library/node/blob/master/0.11/Dockerfile  
ENV NODE_VERSION 0.10.32  
ENV NPM_VERSION 2.1.2  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
# Get Sendak and install node dependencies.  
RUN git clone git://github.com/ozzyjohnson/Sendak.git && \  
cd Sendak && \  
npm install  
  
# Default command.  
CMD ["bash"]  

