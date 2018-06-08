FROM buildpack-deps  
  
# Get up to date, install the bare necessities  
# Create "strongloop" user  
# DANGEROUS: this is a dev convenience container, everyone has sudo access  
RUN DEBIAN_FRONTEND=noninteractive sh -c '( \  
apt-get update -q && \  
apt-get install -y -q curl wget vim man-db ssh bash-completion sudo && \  
apt-get clean && apt-get autoclean)' > /dev/null && \  
useradd -ms /bin/bash strongloop && \  
chown -R strongloop /usr/local && \  
echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Set up some semblance of an environment  
WORKDIR /home/strongloop  
ENV HOME /home/strongloop  
USER strongloop  
  
ENV IOJS_REF v1.8.1  
RUN curl -SLO "https://github.com/iojs/io.js/archive/$IOJS_REF.tar.gz" \  
&& mkdir -p /usr/local/src/node /usr/local/etc \  
&& tar -xzf "$IOJS_REF.tar.gz" -C /usr/local/src/node --strip-components=1 \  
&& (cd /usr/local/src/node && ./configure && make -j4 V= install) \  
&& rm -rf /usr/local/src/node \  
&& npm install -g strongloop \  
&& npm cache clear \  
&& slc --version  
  
# Default to a login shell  
CMD ["/bin/bash", "--login"]  

