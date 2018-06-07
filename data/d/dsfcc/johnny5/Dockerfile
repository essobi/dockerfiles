FROM ubuntu:14.04  
# Install Dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
build-essential \  
pkg-config \  
git \  
python \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Node  
ENV NODE_VERSION 0.10.34  
ENV NPM_VERSION 2.1.12  
RUN gpg --keyserver pgp.mit.edu --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D  
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
  
# Install Hubot  
RUN npm install -g coffee-script@1.8.0 hubot@2.8.3  
  
# Create Hubot  
RUN mkdir /app  
WORKDIR /app  
RUN hubot --create johnny5  
WORKDIR /app/johnny5  
  
# Install hubot-slack  
RUN npm install hubot-slack --save && npm install  
  
# Set Hubot Options  
# HTTP Listener listen port 9980  
ENV PORT 9980  
EXPOSE 9980  
# Add Scripts  
RUN npm install hubot-devops-reactions --save \  
&& npm install hubot-plusplus --save \  
&& npm install hubot-redis-brain --save \  
&& npm install  
  
ADD external-scripts.json /app/johnny5/external-scripts.json  
ADD hubot-scripts.json /app/johnny5/hubot-scripts.json  
  
# Run Hubot  
ENTRYPOINT ["bin/hubot", "-a", "slack"]  

