FROM fluent/fluentd:edge  
LABEL maintainer="Peter Teich <info@pteich.de>"  
  
RUN apk add \--update ca-certificates openssl && update-ca-certificates \  
&& apk add \--virtual .build-deps \  
sudo build-base ruby-dev \  
&& sudo gem install gelf fluent-plugin-gelf-hs fluent-plugin-docker-metrics
docker-api lru_redux \  
&& sudo gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
RUN cd /fluentd/plugins && \  
wget https://raw.githubusercontent.com/itorres/fluent-plugin-docker-
format/master/lib/fluent/plugin/out_docker_format.rb && \  
wget https://raw.githubusercontent.com/rrudduck/fluent-plugin-
docker_metadata_filter/master/lib/fluent/plugin/filter_docker_metadata.rb

