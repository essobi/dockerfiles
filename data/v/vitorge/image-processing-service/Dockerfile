FROM continuumio/miniconda3  
  
WORKDIR /src  
  
# Install APT dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
dirmngr \  
gnupg \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y --no-install-recommends \  
libgtk2.0-dev \  
nodejs \  
unzip \  
&& rm -rf /tmp/* /var/lib/apt/lists/*  
  
# Install GOSU for stepping down from root  
ENV GOSU_VERSION 1.10  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# Copy files  
COPY . /src  
  
# Install global npm dependencies and app  
RUN npm install -g yarn nodemon \  
&& yarn install  
  
# Download model  
RUN mkdir /model \  
&& wget -qO- -O /model/model_frcnn.zip
https://www.dropbox.com/s/4aaumoidekk8t8s/model_frcnn.zip \  
&& unzip -o /model/model_frcnn.zip -d /model \  
&& rm /model/model_frcnn.zip  
  
# Install Anaconda dependencies  
RUN conda install -y scikit-image scikit-learn opencv keras=2.1.4
tensorflow=1.5.0 \  
&& conda clean -a -y  
  
# Patch entrypoint  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Run node server  
CMD ["NODE_PATH=.", "node", "server/"]  

