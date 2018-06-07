FROM debian:jessie  
  
# verify gpg and sha256: http://nodejs.org/dist/v0.10.30/SHASUMS256.txt.asc  
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"  
# gpg: aka "Julien Gilli <jgilli@fastmail.fm>"  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
ENV NODE_VERSION 0.6.12  
ENV NPM_VERSION 1.1.4  
  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH  
ENV PATH /usr/local/lib/node_modules/:$PATH  
  
RUN buildDeps='build-essential python g++ libssl-dev curl ca-certificates' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps openssl --no-install-
recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/node \  
&& curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz" \  
# for our purposes, we don't care if it's verified.  
#&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
#&& gpg --verify SHASUMS256.txt.asc \  
#&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzvf "node-v$NODE_VERSION.tar.gz" -C /usr/src/node --strip-
components=1 \  
&& rm "node-v$NODE_VERSION.tar.gz" \  
&& cd /usr/src/node \  
&& ./configure --openssl-libpath=/usr/lib/ssl \  
&& make \  
&& make install \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& npm cache clear  
  
CMD [ "node" ]  

