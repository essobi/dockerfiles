FROM oraclelinux:7-slim as java8  
  
RUN yum install gzip tar curl -y && rm -rf /var/cache/yum  
  
ENV JAVA_VERSION=8u172 \  
JAVA_BNUMBER=11 \  
JAVA_SEMVER=1.8.0_172 \  
JAVA_HOME=/opt/jre-home \  
JAVA_HASH=a58eab1ec242421181065cdc37240b08 \  
TIMEZONE=America/New_York  
  
  
ENV PATH=$PATH:$JAVA_HOME/bin  
RUN cd / \  
&& curl --header "Cookie: oraclelicense=accept-securebackup-cookie" -fSL \  
http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-b$JAVA_BNUMBER/$JAVA_HASH/server-jre-$JAVA_VERSION-
linux-x64.tar.gz \  
-o server-jre-$JAVA_VERSION-linux-x64.tar.gz \  
&& tar -zxvf server-jre-$JAVA_VERSION-linux-x64.tar.gz -C /opt \  
&& rm server-jre-$JAVA_VERSION-linux-x64.tar.gz \  
&& ln -s /opt/jdk$JAVA_SEMVER/ /opt/jre-home;  
  
FROM java8 as tomcat8  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN groupadd -r tomcat && useradd -r -g tomcat tomcat  
RUN mkdir -p "$CATALINA_HOME" && chown tomcat:tomcat "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS  
RUN for key in \  
05AB33110949707C93A279E3D3EFE6B686867BA6 \  
07E48665A34DCAFAE522E5E6266191C37C037D42 \  
47309207D818FFD8DCD3F83F1931D684307A10A5 \  
541FBE7D8F78B25E055DDEE13C370389288584E7 \  
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
713DA88BE50911535FE716F5208B0AB1D63011C7 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
9BA44C2621385CB966EBA586F72C284D731FABEE \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV TOMCAT_MAJOR=8  
ENV TOMCAT_VERSION=8.0.52  
ENV
TOMCAT_TGZ_URL=https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
  
RUN set -x \  
&& curl -fSL $TOMCAT_TGZ_URL -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
&& rm -rf webapps/* \  
&& chown -R tomcat:tomcat $CATALINA_HOME  
  
FROM tomcat8 as banner9-selfservice  
  
ENV XMS=2g XMX=4g
BANNERDB_JDBC=jdbc:oracle:thin:@//oracle.example.edu:1521/prod \  
BANPROXY_USERNAME=banproxy \  
BANPROXY_INITALSIZE=25 \  
BANPROXY_MAXTOTAL=400 \  
BANPROXY_MAXIDLE=-1 \  
BANPROXY_MAXWAIT=30000  
ENV JAVA_OPTS -Duser.timezone=\$TIMEZONE -XX:+UseParallelGC  
ENV CATALINA_OPTS -Xms\$XMS -Xmx\$XMX -Dlog4j.configuration=config.properties  
  
ADD
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/ojdbc7/12.1.0.2/ojdbc7-12.1.0.2.jar
/usr/local/tomcat/lib/ojdbc7.jar  
ADD
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/xdb6/12.1.0.2/xdb6-12.1.0.2.jar
/usr/local/tomcat/lib/xdb6.jar  
ADD
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/ucp/12.1.0.2/ucp-12.1.0.2.jar
/usr/local/tomcat/lib/ucp.jar  
  
RUN cd /usr/local/tomcat/lib/ \  
&& curl
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/ojdbc7/12.1.0.2/ojdbc7-12.1.0.2.jar.sha1
--output ojdbc7.jar.sha1 \  
&& echo -n " ojdbc7.jar" >> ojdbc7.jar.sha1 \  
&& sha1sum -c ojdbc7.jar.sha1 \  
&& curl
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/xdb6/12.1.0.2/xdb6-12.1.0.2.jar.sha1
--output xdb6.jar.sha1 \  
&& echo -n " xdb6.jar" >> xdb6.jar.sha1 \  
&& sha1sum -c xdb6.jar.sha1 \  
&& curl
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/ucp/12.1.0.2/ucp-12.1.0.2.jar.sha1
--output ucp.jar.sha1 \  
&& echo -n " ucp.jar" >> ucp.jar.sha1 \  
&& sha1sum -c ucp.jar.sha1 \  
&& rm *.sha1 \  
&& chown tomcat:tomcat *.jar && chmod +r *.jar  
  
COPY context.xml /usr/local/tomcat/conf/context.xml  
COPY server.xml /usr/local/tomcat/conf/server.xml  
COPY run.sh /usr/local/tomcat/bin  
  
# Configure logging to forward tomcat logs to docker log collector  
COPY logging.properties /usr/local/tomcat/conf/logging.properties  
RUN ln -s /dev/stderr /usr/local/tomcat/logs/localhost.log  
RUN ln -s /dev/stderr /usr/local/tomcat/logs/stacktrace.log  
  
RUN chown -R tomcat:tomcat /usr/local/tomcat && chmod +x
/usr/local/tomcat/bin/run.sh  
EXPOSE 8080  
USER tomcat  
CMD ["bin/run.sh"]  

