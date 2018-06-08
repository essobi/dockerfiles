FROM codefresh/slimbuntu:latest  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
ENV NODE_VERSION 0.12.7  
ENV NPM_VERSION 2.11.3  
EXPOSE 4873  
WORKDIR /opt/sinopia  
RUN buildDeps='curl ca-certificates python' \  
&& set -x \  
&& adduser --disabled-password --gecos "" sinopia \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install sinopia \  
&& chown -R sinopia:sinopia /opt/sinopia \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
USER sinopia  
COPY config.yaml /opt/sinopia/config.yaml  
WORKDIR /opt  
CMD ["./sinopia/node_modules/sinopia/bin/sinopia"]  

