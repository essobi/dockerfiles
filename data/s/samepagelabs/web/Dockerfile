FROM java:8  
# Installs Ant  
ENV ANT_VERSION 1.9.7  
RUN cd && \  
wget http://www.us.apache.org/dist//ant/binaries/apache-ant-$ANT_VERSION-
bin.tar.gz && \  
tar -xzf apache-ant-$ANT_VERSION-bin.tar.gz && \  
mv apache-ant-$ANT_VERSION /opt/ant && \  
rm apache-ant-$ANT_VERSION-bin.tar.gz  
  
RUN apt-get update && apt-get --yes install rubygems ruby-dev make g++  
RUN gem install compass  
  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.31/SHASUMS256.txt.asc  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
# gpg: aka "Julien Gilli <jgilli@fastmail.fm>"  
RUN set -ex \  
&& for key in \  
7937DFD2AB06298B2293C3187D33FF9D0246406D \  
114F43EE0176B71C7BC219DD50A3051F888C628D \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NODE_VERSION 0.10.40  
ENV NPM_VERSION 2.13.3  
RUN wget "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& wget "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin:/usr/local/bin  
  
CMD ["bash", "-c", "echo -n 'Node version: ' ; node --version; ant -version"]  

