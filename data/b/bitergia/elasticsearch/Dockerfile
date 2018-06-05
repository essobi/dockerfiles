#  
# ElasticSearch Dockerfile  
#  
# Deliberately stolen from: https://github.com/dockerfile/elasticsearch  
#  
# Pull base image.  
FROM anapsix/alpine-java  
  
# Install ElasticSearch.  
RUN apk update && apk add ca-certificates wget && apk add ca-certificates curl
&& update-ca-certificates  
RUN \  
mkdir /tmp/es && \  
cd /tmp/es && \  
wget
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.1.0.tar.gz
&& \  
tar xvzf elasticsearch-*.tar.gz && \  
rm -f elasticsearch-*.tar.gz && \  
mv /tmp/es/elasticsearch-* /elasticsearch && \  
rm -rf /tmp/es  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Mount elasticsearch.yml config  
COPY elasticsearch.yml /elasticsearch/config/  
# Install Search-Guard plugin  
RUN /elasticsearch/bin/elasticsearch-plugin install -b com.floragunn:search-
guard-6:6.1.0-21.0 && \  
cd /elasticsearch/plugins/search-guard-6/tools/ && \  
rm install_demo_configuration.sh && \  
wget https://raw.githubusercontent.com/floragunncom/search-
guard/master/tools/install_demo_configuration.sh && \  
chmod 755 install_demo_configuration.sh && \  
# This is for the elastic container 6.1.0 which grep does not support --quiet  
sed -i 's/\\-\\-quiet/\\-q/' /elasticsearch/plugins/search-
guard-6/tools/install_demo_configuration.sh && \  
./install_demo_configuration.sh -y && \  
echo "searchguard.enterprise_modules_enabled: false" >> \  
/elasticsearch/config/elasticsearch.yml  
# Add default roles  
ADD sg_roles_mapping.yml /usr/share/elasticsearch/plugins/search-
guard-6/sgconfig/sg_roles_mapping.yml  
  
# Change log level INFO->DEBUG  
#RUN TMP_FILE=`mktemp /tmp/config.XXXXXXXXXX` && \  
# sed -e "s/INFO/INFO/" /elasticsearch/config/logging.yml > $TMP_FILE && \  
# mv $TMP_FILE /elasticsearch/config/logging.yml  
# Define working directory.  
WORKDIR /data  
  
RUN adduser -D -u 1000 esuser  
RUN chown -R esuser /elasticsearch  
USER esuser  
  
# Remote debugger  
ENV ES_JAVA_OPTS
"-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8000"  
ENV PATH /elasticsearch/bin:$PATH  
  
COPY ./docker-entrypoint.sh /  
  
# Expose ports.  
# - 8000: Debug  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 8000  
#EXPOSE 9300  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["elasticsearch"]  

