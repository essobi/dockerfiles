#  
# OHIE-FR  
#  
#  
FROM uwitech/ohie-base  
  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y git build-essential curl wget software-properties-common  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
  
# Install Tomcat  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS  
ENV GPG_KEYS 05AB33110949707C93A279E3D3EFE6B686867BA6
07E48665A34DCAFAE522E5E6266191C37C037D42
47309207D818FFD8DCD3F83F1931D684307A10A5
541FBE7D8F78B25E055DDEE13C370389288584E7
61B832AC2F1C5A90F0F9B00A1C506407564C17A3
713DA88BE50911535FE716F5208B0AB1D63011C7
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED
9BA44C2621385CB966EBA586F72C284D731FABEE
A27677289986DB50844682F8ACB77FC2E86E29AC
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
RUN set -ex; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.15  
ENV TOMCAT_TGZ_URL
http://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --verify tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
&& mkdir -p $CATALINA_HOME/ROOT/dhis-web-core-resource  
  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
COPY conf/hibernate.properties /opt/dhis2/config/hibernate.properties  
COPY conf/dhis.conf /opt/dhis2/config/dhis.conf  
COPY manifest.webapp $CATALINA_HOME/ROOT/dhis-web-core-
resource/manifest.webapp  
  
RUN wget https://s3-eu-west-1.amazonaws.com/releases.dhis2.org/2.26/dhis.war
-O $CATALINA_HOME/webapps/ROOT.war  
RUN chmod 0600 /opt/dhis2/config/dhis.conf  
  
# Add admin/admin user  
ADD tomcat-users.xml $CATALINA_HOME/conf/  
  
EXPOSE 8080  
EXPOSE 8009  
RUN echo "export JAVA_OPTS=$JAVA_OPTS\nexport DHIS2_HOME='/opt/dhis2/config'"
>> $CATALINA_HOME/bin/setenv.sh  
  
COPY cmd.sh /cmd.sh  
RUN chmod +x /cmd.sh  
  
# Launch Tomcat  
CMD /cmd.sh  

