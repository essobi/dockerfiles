#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
FROM stocksoftware/java:jdk8  
  
ENV PATH=/opt/elasticsearch/bin:$PATH \  
ES_VERSION=2.3.4  
# Setup elasticsearch user and group  
# Install elasticsearch into /opt/elasticsearch  
# Configure elasticsearch runtime  
# Setup elasticsearch data directory  
RUN addgroup -S elasticsearch -g 600 && \  
adduser -D -H -s /bin/false -h /opt/elasticsearch -G elasticsearch -u 200 -S
elasticsearch && \  
mkdir -p /opt && \  
curl -Ls
http://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ES_VERSION/elasticsearch-$ES_VERSION.tar.gz
| tar -xz -C /opt && \  
mv /opt/elasticsearch-$ES_VERSION /opt/elasticsearch && \  
mkdir -p /opt/elasticsearch/config/scripts /opt/elasticsearch/plugins
/srv/elasticsearch/data /srv/elasticsearch/logs  
  
COPY elasticsearch.yml /opt/elasticsearch/elasticsearch.yml  
COPY logging.yml /opt/elasticsearch/config/  
  
RUN chown -R elasticsearch:elasticsearch /srv/elasticsearch /opt/elasticsearch  
  
VOLUME /srv/elasticsearch  
  
EXPOSE 9200  
USER elasticsearch:elasticsearch  
  
WORKDIR /opt/elasticsearch  
  
CMD ["/opt/elasticsearch/bin/elasticsearch", "-Des.network.host=0.0.0.0",
"-Dpath.data=/srv/elasticsearch/data", "-Dpath.logs=/srv/elasticsearch/logs"]  

