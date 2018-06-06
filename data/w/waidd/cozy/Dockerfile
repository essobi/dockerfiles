FROM node:6-slim  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install --quiet --assume-yes --no-install-recommends \  
python \  
postfix \  
openssl \  
git \  
imagemagick \  
curl \  
wget \  
sqlite3 \  
sudo \  
build-essential \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Prepare cozy directories  
RUN useradd -MU cozy \  
&& useradd -MU cozy-data-system \  
&& useradd -MU cozy-home \  
&& mkdir /etc/cozy \  
&& chown -hR cozy /etc/cozy  
  
# Install cozy core modules  
RUN npm install -g coffee-script cozy-monitor cozy-controller  
  
ADD start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
ENV NODE_ENV=production \  
COUCH_HOST=couchdb \  
COUCH_PORT=5984  
EXPOSE 9103 9014 9014  
WORKDIR /usr/local/lib/node_modules/cozy-controller/build/  
  
CMD [ "/usr/local/bin/start.sh" ]  
  
# exposer les dossiers de stockage

