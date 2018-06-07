FROM grossws/java  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
WORKDIR /opt/solr  
  
ARG UID=200  
RUN useradd -r --create-home -g nobody -u $UID solr  
  
ARG SOLR_VERSION=7.3.0  
ARG
SOLR_TGZ_URL=https://www.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz  
  
RUN gpg --recv-keys $(curl
"https://www.apache.org/dist/lucene/solr/${SOLR_VERSION}/KEYS" | gpg --with-
fingerprint --with-colons | grep "^fpr" | cut -d: -f10) \  
&& NEAREST_SOLR_TGZ_URL=$(curl -sSL
http://www.apache.org/dyn/closer.cgi/${SOLR_TGZ_URL#https://www.apache.org/dist/}\?asjson\=1
\  
| awk '/"path_info": / { pi=$2; }; /"preferred":/ { pref=$2; }; END { print
pref " " pi; };' \  
| sed -r -e 's/^"//; s/",$//; s/" "//') \  
&& echo "Nearest mirror: $NEAREST_SOLR_TGZ_URL" \  
&& curl -sSL "$NEAREST_SOLR_TGZ_URL" -o solr.tar.gz \  
&& curl -sSL $SOLR_TGZ_URL.asc -o solr.tar.gz.asc \  
&& gpg --verify solr.tar.gz.asc solr.tar.gz \  
&& tar xvf solr.tar.gz -C /opt/solr --strip-components=1
solr-$SOLR_VERSION/bin/{oom_solr.sh,post,solr,solr.in.sh} \  
solr-$SOLR_VERSION/{LICENSE.txt,NOTICE.txt,licenses} \  
solr-$SOLR_VERSION/server/{contexts,etc,lib,modules,resources,scripts,solr-
webapp,start.jar} \  
&& tar xvf solr.tar.gz -C /opt/solr --strip-components=3
solr-$SOLR_VERSION/server/solr/solr.xml \  
&& rename .txt '' *.txt \  
&& echo "name = core0" > core.properties \  
&& rm solr.tar.gz*  
  
RUN JETTY_VERSION=$(find /opt/solr/server/lib -name 'jetty-server-*.jar' | sed
's|.jar$||; s|^.*/jetty-server-||;') \  
&& echo "jetty version: $JETTY_VERSION" \  
&&
JETTY_SRC_BASE_URL=https://raw.githubusercontent.com/eclipse/jetty.project/jetty-$JETTY_VERSION/jetty-
server/src/main/config/etc/jetty-gzip.xml \  
&& curl -sSL -o /opt/solr/server/etc/jetty-gzip.xml
$JETTY_SRC_BASE_URL/etc/jetty-gzip.xml \  
&& curl -sSL -o /opt/solr/server/modules/gzip.mod
$JETTY_SRC_BASE_URL/modules/gzip.mod \  
&& sed -i -r -e 's|(SOLR_JETTY_CONFIG\\+=\\("--
module=)(https?)("\\))|\1\2,gzip\3|' /opt/solr/bin/solr  
  
VOLUME ["/opt/solr/data"]  
EXPOSE 8983  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["solr"]  
  

