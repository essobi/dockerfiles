# The container includes:  
#  
# azukiapp/ruby:  
# * Node 0.12.7  
#  
FROM azukiapp/web-based  
MAINTAINER Azuki <support@azukiapp.com>  
  
# verify gpg and sha256: http://nodejs.org/dist/v0.12.0/SHASUMS256.txt.as7  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
RUN gpg --keyserver pgp.mit.edu --recv-keys
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
ENV NODE_VERSION 0.12.7  
ENV NPM_VERSION 2.14.1  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
CMD [ "node" ]  

