FROM wnameless/oracle-xe-11g:latest  
  
MAINTAINER Jaime Sánchez from Digibis <jaime.sanchez@digibis.com>  
  
  
  
ENV DUMP_DIR /dump  
ENV TABLE_SPACE_SIZE 100M  
  
#Variables de configuración para Oracle XE  
ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe  
ENV PATH $ORACLE_HOME/bin:$PATH  
ENV ORACLE_SID XE  
  
#Creamos el directorio donde va el dump de base de datos  
RUN mkdir $DUMP_DIR  
  
#Variables de configuración para tomcat 7  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.68  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS  
RUN set -ex \  
&& for key in \  
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
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update && \  
apt-get install -y oracle-java8-installer openssh-server curl gzip nano && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
#Borramos el tomcat users original  
RUN rm $CATALINA_HOME/conf/tomcat-users.xml  
  
#Copiamos el tomcat users con el manager de GUI a admin:admin, y el driver de
oracle a libs  
COPY filesconfig/tomcat-users.xml $CATALINA_HOME/conf/tomcat-users.xml  
COPY filesconfig/ojdbc6.jar $CATALINA_HOME/lib/ojdbc6.jar  
  
#Cambiamos el puerto del tomcat al 80 para que no tenga conlictos con el
puerto del APEX  
RUN sed -i -e 's/8080/80/g' $CATALINA_HOME/conf/server.xml  
  
#Se inicia primero el oracle XE heredado, despues tomcat y por último el ssh  
CMD /usr/sbin/startup.sh && $CATALINA_HOME/bin/startup.sh && /usr/sbin/sshd -D

