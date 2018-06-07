FROM grossws/java  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
ENV CATALINA_HOME=/opt/tomcat  
  
ARG UID=200  
RUN useradd -r --create-home -g nobody -u $UID tomcat  
  
# $CATALINA_HOME impicitly created adding these files  
ADD entrypoint.sh server.xml logging.properties $CATALINA_HOME/  
  
WORKDIR $CATALINA_HOME  
  
ARG TOMCAT_MAJOR=8  
ARG TOMCAT_VERSION=8.0.50  
ARG
TOMCAT_TGZ_URL=https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN gpg --recv-keys $(curl
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS | gpg --with-
fingerprint --with-colons | grep fpr | cut -d: -f10) \  
&& NEAREST_TOMCAT_TGZ_URL=$(curl -sSL
http://www.apache.org/dyn/closer.cgi/${TOMCAT_TGZ_URL#https://www.apache.org/dist/}\?asjson\=1
\  
| awk '/"path_info": / { pi=$2; }; /"preferred":/ { pref=$2; }; END { print
pref " " pi; };' \  
| sed -r -e 's/^"//; s/",$//; s/" "//') \  
&& echo "Nearest mirror: $NEAREST_TOMCAT_TGZ_URL" \  
&& curl -sSL "$NEAREST_TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -sSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --verify tomcat.tar.gz.asc tomcat.tar.gz \  
&& tar -xf tomcat.tar.gz --strip-components=1 \  
&& mkdir -p conf/Catalina/localhost \  
&& rm -f bin/*.bat \  
&& rm -rf webapps/* \  
&& rm tomcat.tar.gz* \  
&& mv logging.properties server.xml $CATALINA_HOME/conf/ \  
&& mv $CATALINA_HOME/entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["tomcat"]  
  

