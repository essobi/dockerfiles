FROM debian:wheezy  
  
ENV KIBANA_DOWNLOAD_SHA1=c925f75cd5799bfd892c7ea9c5936be10a20b119  
ENV
KIBANA_DOWNLOAD_URL=https://download.elastic.co/kibana/kibana/kibana-4.0.2-linux-x64.tar.gz  
  
RUN buildDeps='curl ca-certificates'; \  
set -x \  
&& apt-get update \  
&& apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src/app \  
&& curl -sSL "$KIBANA_DOWNLOAD_URL" -o kibana.tar.gz \  
&& echo "$KIBANA_DOWNLOAD_SHA1 *kibana.tar.gz" | sha1sum -c - \  
&& tar -xzf kibana.tar.gz -C /usr/src/app --strip-components=1 \  
&& rm kibana.tar.gz \  
&& apt-get purge -y --auto-remove $buildDeps  
  
WORKDIR /usr/src/app  
  
ADD kibana.yml /usr/src/app/kibana.yml  
ADD run.sh /usr/src/app/bin/run.sh  
  
EXPOSE 5601  
CMD ["bin/run.sh"]  

