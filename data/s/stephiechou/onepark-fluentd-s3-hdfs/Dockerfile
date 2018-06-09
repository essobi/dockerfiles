  
FROM fluent/fluentd:latest  
MAINTAINER Stéphie <stephanie.chhim@onepark.fr>  
  
RUN apk add --update --virtual .build-deps \  
sudo build-base ruby-dev \  
&& sudo gem install \fluent-plugin-s3 \  
  
&& sudo gem sources --clear-all \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
/home/fluent/.gem/ruby/2.3.0/cache/*.gem  
  
EXPOSE 24224  
RUN mkdir -p /var/log/fluent  
RUN chmod 0777 /var/log/fluent  
RUN mkdir /conf  
WORKDIR /conf  
  
COPY conf/fluent.conf fluent.conf  
  
# Start an instance of Fluentd  
CMD fluentd -c fluent.conf  

