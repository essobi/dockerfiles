# GeoServer 2.8.2  
# Oracle JRE 1.7  
# JAI 1.1.3  
# ImageIO 1.1  
# Tomcat 8.0.30  
  
FROM centos:7  
MAINTAINER Maxime Werlen maxime@werlen.fr  
  
#
-------------------------------------------------------------------------------------------------------------  
# Install Java.  
#
-------------------------------------------------------------------------------------------------------------  
RUN curl -LO 'http://download.oracle.com/otn-
pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm' \  
-H 'Cookie: oraclelicense=accept-securebackup-cookie'  
  
RUN rpm -i jdk-7u51-linux-x64.rpm  
RUN rm jdk-7u51-linux-x64.rpm  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/java/default/  
  
#
----------------------------------------------------------------------------------------  
# Install JAI and JAI Image I/O  
#
----------------------------------------------------------------------------------------  
WORKDIR /tmp  
RUN curl
http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-
amd64.tar.gz > jai-1_1_3-lib-linux-amd64.tar.gz && \  
curl http://download.java.net/media/jai-
imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64.tar.gz >
jai_imageio-1_1-lib-linux-amd64.tar.gz && \  
gunzip -c jai-1_1_3-lib-linux-amd64.tar.gz | tar xf \- && \  
gunzip -c jai_imageio-1_1-lib-linux-amd64.tar.gz | tar xf \- && \  
mv /tmp/jai-1_1_3/lib/jai_core.jar $JAVA_HOME/jre/lib/ext/ && \  
mv /tmp/jai-1_1_3/lib/jai_codec.jar $JAVA_HOME/jre/lib/ext/ && \  
mv /tmp/jai-1_1_3/lib/mlibwrapper_jai.jar $JAVA_HOME/jre/lib/ext/ && \  
mv /tmp/jai-1_1_3/lib/libmlib_jai.so $JAVA_HOME/jre/lib/amd64/ && \  
mv /tmp/jai_imageio-1_1/lib/jai_imageio.jar $JAVA_HOME/jre/lib/ext/ && \  
mv /tmp/jai_imageio-1_1/lib/clibwrapper_jiio.jar $JAVA_HOME/jre/lib/ext/ && \  
mv /tmp/jai_imageio-1_1/lib/libclib_jiio.so $JAVA_HOME/jre/lib/amd64/ && \  
rm /tmp/jai-1_1_3-lib-linux-amd64.tar.gz && \  
rm -r /tmp/jai-1_1_3 && \  
rm /tmp/jai_imageio-1_1-lib-linux-amd64.tar.gz && \  
rm -r /tmp/jai_imageio-1_1  
#
--------------------------------------------------------------------------------------------------------------  
# Unlimited security  
#
---------------------------------------------------------------------------------------------------------------  
COPY local_policy.jar $JAVA_HOME/jre/lib/security/local_policy.jar  
COPY US_export_policy.jar $JAVA_HOME/jre/lib/security/US_export_policy.jar  
#
--------------------------------------------------------------------------------------------------------------  
# Install Tomcat  
#
--------------------------------------------------------------------------------------------------------------  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \  
05AB33110949707C93A279E3D3EFE6B686867BA6 \  
07E48665A34DCAFAE522E5E6266191C37C037D42 \  
47309207D818FFD8DCD3F83F1931D684307A10A5 \  
541FBE7D8F78B25E055DDEE13C370389288584E7 \  
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
80FF76D88A969FE46108558A80B953A041E49465 \  
8B39757B1D8A994DF2433ED58B3A601F08C975E5 \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
B3F49CD3B9BD2996DA90F817ED3873F5D3262722 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.30  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --verify tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
&& rm -rf $CATALINA_HOME/webapps/*  
  
# Set Heap Settings for Tomcat  
# See: http://docs.geoserver.org/stable/en/user/production/container.html  
ENV CATALINA_OPTS -Xmx1024m -Xms48m -XX:SoftRefLRUPolicyMSPerMB=36000
-XX:MaxPermSize=512m -XX:+UseParallelGC -server  
  
#
-------------------------------------------------------------------------------  
# Install geoserver  
#
---------------------------------------------------------------------------------  
  
WORKDIR $CATALINA_HOME/webapps/geoserver  
RUN curl
http://netix.dl.sourceforge.net/project/geoserver/GeoServer/2.8.2/geoserver-2.8.2-war.zip
> /tmp/geoserver.zip; \  
jar xvf /tmp/geoserver.zip geoserver.war && jar xvf geoserver.war && rm
geoserver.war  
  
# ---------------------------------------  
# Change user  
# --------------------------------------  
  
RUN useradd -M -r geoserver && chown -R geoserver:geoserver $CATALINA_HOME  
USER geoserver  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

