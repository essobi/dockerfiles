FROM docker.elastic.co/kibana/kibana-ubuntu-base:latest  
ARG X_PACK_URL=https://snapshots.elastic.co/downloads/kibana-
plugins/x-pack/x-pack-6.0.0-alpha1-SNAPSHOT.zip  
ENV PATH=/usr/share/kibana/bin:$PATH  
  
EXPOSE 5601  
RUN usermod --home /usr/share/kibana kibana  
RUN apt-get -y update \  
&& apt-get -y install ruby-dev build-essential git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem install pleaserun -v 0.0.24 \  
&& curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash \  
&& true  
  
WORKDIR /tmp/kibana-src  
COPY . /tmp/kibana-src  
RUN . /root/.nvm/nvm.sh \  
&& nvm install $(cat .node-version) \  
&& npm install \  
&& npm run build -- --skip-os-packages --release \  
&& true  
  
RUN mkdir -p /usr/share/kibana \  
&& chown -R kibana: /usr/share/kibana \  
&& true  
  
USER kibana  
WORKDIR /usr/share/kibana  
RUN curl -Ls file:///tmp/kibana-
src/target/kibana-6.0.0-alpha1-linux-x86_64.tar.gz \  
| tar --strip-components=1 -zxf - \  
&& kibana-plugin install ${X_PACK_URL} \  
&& true  
  
ENTRYPOINT ["/usr/share/kibana/bin/kibana"]  

