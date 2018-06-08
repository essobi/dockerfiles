FROM fluent/fluentd:debian  
MAINTAINER Oluwaseun Obajobi <oba@obajobi.com>  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libsystemd0 && \  
buildDeps="build-essential make ruby-dev" && \  
apt-get install -y --no-install-recommends $buildDeps && \  
fluent-gem install --no-ri --no-rdoc fluent-plugin-systemd -v 0.3.0 && \  
fluent-gem install --no-ri --no-rdoc fluent-plugin-gelf-hs -v 1.0.3 && \  
fluent-gem install --no-ri --no-rdoc fluent-plugin-kubernetes_metadata_filter
-v 0.28.0 && \  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
$buildDeps && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem  
  
COPY ./run.sh /run.sh  
RUN chmod a+x /run.sh  
  
WORKDIR /home/fluent  
  
ENTRYPOINT [ "/run.sh"]  

