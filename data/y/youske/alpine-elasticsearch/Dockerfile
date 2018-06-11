# alpine linux with elasticsearch  
#  
FROM youske/alpine-java:latest  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
ENV ELASTICSEARCH_VERSION=2.3.0  
ENV ELASTICSEARCH_BASE=/elasticsearch  
ENV DFILE=elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz  
ENV
DOWNLOAD_URL=https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/${ELASTICSEARCH_VERSION}/${DFILE}  
ENV PACKAGE="glibc glibc-bin" \  
BUILDPACKAGE="wget build-base linux-headers" \  
PATH=${ELASTICSEARCH_BASE}/bin:$PATH  
  
# elasticsearch user  
RUN addgroup elasticsearch && adduser -S elasticsearch -h /elasticsearch -G
elasticsearch -D -H  
  
RUN apk upgrade --no-cache && apk add ${BUILDPACKAGE} \--no-cache -t buildtool  
  
RUN wget -q --no-check-certificate ${DOWNLOAD_URL} -O- | tar -zx && \  
mv elasticsearch-${ELASTICSEARCH_VERSION} ${ELASTICSEARCH_BASE} && \  
chown -R root:elasticsearch ${ELASTICSEARCH_BASE}  
  
COPY config ${ELASTICSEARCH_BASE}/config  
  
RUN mkdir -p ${ELASTICSEARCH_BASE}/plugins && \  
mkdir -p /eslogs && chown -R elasticsearch:elasticsearch /eslogs && \  
mkdir -p /esdata && chown -R elasticsearch:elasticsearch /esdata  
  
# plugin install river-csv -url https://github.com/AgileWorksOrg &&  
RUN echo "hoge" && \  
# plugin install elasticsearch/elasticsearch-river-twitter/2.6.0 && \  
# plugin install elasticsearch/kibana && \  
# plugin install elasticsearch/elasticsearch-lang-python/2.7.0 && \  
# plugin install elasticsearch/elasticsearch-lang-javascript/2.7.0 && \  
plugin install polyfractal/elasticsearch-inquisitor && \  
# plugin install elasticsearch/elasticsearch-analysys-kuromoji/1.6.0 && \  
plugin install mobz/elasticsearch-head && \  
# plugin install com.github.kzwang/elasticsearch-image/1.2.0 && \  
# plugin install royrusso/marvel && \  
plugin install appbaseio/dejaVu && \  
plugin install royrusso/elasticsearch-HQ/v.2.0.0  
  
RUN apk del buildtool --no-cache && rm -fr /tmp/* /var/cache/apk/*  
  
EXPOSE 9200 9300  
USER elasticsearch  
WORKDIR ${ELASTICSEARCH_BASE}  
ENTRYPOINT ["switch","shell=/bin/bash","--","/init"]  
CMD ["elasticsearch","-Des.network.host=0.0.0.0"]  
  

