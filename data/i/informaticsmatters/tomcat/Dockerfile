FROM debian:stretch  
LABEL maintainer="tdudgeon@informaticsmatters.com"  
  
RUN apt-get update -y &&\  
apt-get upgrade -y &&\  
apt-get install -y --no-install-recommends openjdk-8-jre-headless curl gpg
libapr1 dirmngr &&\  
apt-get clean  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.48  
ENV ARCHIVE apache-tomcat-$TOMCAT_VERSION.tar.gz  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys \  
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
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
  
RUN useradd -u 501 -U -G 0 tomcat  
  
WORKDIR /usr/local  
  
RUN curl -s -o tomcat.tar.gz
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/$ARCHIVE
&&\  
curl -s -o tomcat.tar.gz.asc
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/$ARCHIVE.asc
&&\  
gpg --verify tomcat.tar.gz.asc tomcat.tar.gz &&\  
tar xfz tomcat.tar.gz &&\  
rm tomcat.tar.gz &&\  
mv apache-tomcat-$TOMCAT_VERSION tomcat &&\  
rm tomcat/bin/*.bat &&\  
rm -rf tomcat/webapps/* &&\  
chown -R 501:0 tomcat &&\  
chmod -R g+r tomcat &&\  
chmod g+w tomcat tomcat/logs tomcat/webapps tomcat/temp tomcat/work
tomcat/conf tomcat/bin tomcat/lib  
  
WORKDIR /usr/local/tomcat  
ENV CATALINA_HOME /usr/local/tomcat  
EXPOSE 8080  
USER 501  
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]  
  

