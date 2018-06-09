FROM docker.elastic.co/elasticsearch/elasticsearch:5.3.0  
  
USER root  
  
RUN set -x \  
&& elasticsearch-plugin install --batch discovery-ec2 \  
&& elasticsearch-plugin install --batch repository-s3  
  
ENV DUMB_INIT_VERSION 1.2.0  
RUN set -ex \  
&& apk --no-cache add su-exec \  
&& wget "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64" \  
&& wget "https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/sha256sums" \  
&& grep "dumb-init_${DUMB_INIT_VERSION}_amd64$" sha256sums | sha256sum -c \  
&& rm sha256sums \  
&& mv dumb-init_${DUMB_INIT_VERSION}_amd64 /usr/bin/dumb-init \  
&& chmod +x /usr/bin/dumb-init  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bin/es-docker"]  

