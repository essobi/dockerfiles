FROM node:4.5  
ENV DEBIAN_FRONTEND=noninteractive \  
NODE_ENV=production  
  
RUN apt-get update \  
&& apt-get install --quiet --assume-yes --no-install-recommends \  
build-essential \  
curl \  
imagemagick \  
libffi-dev \  
nano \  
python-dev \  
sqlite3 \  
sudo \  
python-setuptools \  
python-pip \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
git \  
python python-setuptools python-dev libffi-dev \  
libxml2-dev libxslt-dev libyaml-dev libtiff-dev libjpeg-dev zlib1g-dev \  
libfreetype6-dev libwebp-dev build-essential gcc g++ \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install CoffeeScript & Cozy Controller  
RUN npm install -g \  
coffee-script \  
cozy-controller \  
cozy-monitor  
  
# Create Cozy users, without home directories.  
RUN useradd -M cozy \  
&& useradd -M cozy-data-system \  
&& useradd -M cozy-home  
  
# Install Weboob in order to run kresus module  
RUN git clone git://git.symlink.me/pub/weboob/devel.git /tmp/weboob \  
&& cd /tmp/weboob \  
&& python ./setup.py install \  
&& rm -rf /tmp/weboob  
  
ADD init.sh /usr/local/bin/cozy-init.sh  
RUN chmod 755 /usr/local/bin/cozy-init.sh  
  
# Need ENV VARS:  
# Expose port  
EXPOSE 9002 9104  
VOLUME ["/etc/cozy", "/usr/local/cozy", "/usr/local/var/cozy/",
"/usr/local/var/log/cozy"]  
WORKDIR /usr/local/lib/node_modules/cozy-controller/build/  
ENTRYPOINT "/usr/local/bin/cozy-init.sh"  
# CMD [ "node", "server.js" ]  

