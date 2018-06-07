FROM ubuntu  
  
MAINTAINER Frank Foerster <openkm_docker@foersterfrank.de>  
  
# add user openkm (password openkmadmin)  
RUN useradd --password
'$6$d7WGWXVT1$27UG2CfTvKuJTNj4UYzEAxVlLoJ6ia9lRlSIV2nhFpEHqJk0JQfrcrYEmqIdFaNN/IyWWjHC8aBLO1mRDxe3k/'
openkm  
  
# install wget gawk pciutils  
RUN apt-get update && apt-get install -y wget gawk pciutils && apt-get clean  
  
# download and run inxi  
RUN wget -O /tmp/inxi -Nc smxi.org/inxi && chmod +x /tmp/inxi && /tmp/inxi -F  
  
# increase ulimit  
RUN sed -i '/#session[[:space:]]*required[[:space:]]*pam_limits.so/s/^#//;'
/etc/pam.d/su  
RUN sed -i '/# End of file/d' /etc/security/limits.conf && \  
echo "* soft nofile 6084" >> /etc/security/limits.conf && \  
echo "* hard nofile 6084" >> /etc/security/limits.conf && \  
echo "# End of file" >> /etc/security/limits.conf  
  
# install java 1.8  
RUN apt-get install -y openjdk-8-jdk openjdk-8-jre  
  
# install required software  
RUN apt-get -y install libreoffice imagemagick swftools liblog4j1.2-java
libgnumail-java ant curl unzip sudo tar && apt-get clean  
  
#install OCR software and English and German dictionaries  
RUN apt-get install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu &&
apt-get clean  
  
ENV CATALINA_HOME /usr/local/tomcat/  
ENV JAVA_HOME /usr/local/java  
ENV OPENJDK_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre/  
ENV TOMCAT_HOME="$CATALINA_HOME"  
RUN ln -s $OPENJDK_HOME $JAVA_HOME  
RUN wget -O /usr/local/openkm-tomcat-bundle.zip
https://sourceforge.net/projects/openkm/files/6.3.2/openkm-6.3.2-community-
tomcat-bundle.zip/download && unzip /usr/local/openkm-tomcat-bundle.zip -d
/usr/local/ && rm /usr/local/openkm-tomcat-bundle.zip && ln -s $CATALINA_HOME
/opt/openkm  
  
RUN wget -O /tmp/openkm-6.3.3.zip
https://sourceforge.net/projects/openkm/files/6.3.3/OpenKM-6.3.3.zip/download
&& unzip /tmp/openkm-6.3.3.zip -d /tmp/ && mv /tmp/OpenKM.war
$TOMCAT_HOME/webapps/ && rm /tmp/openkm-6.3.3.zip  
RUN sed -i 's|http://www.springframework.org/schema/security/spring-
security-3.1.xsd|http://www.springframework.org/schema/security/spring-
security-3.2.xsd|' $TOMCAT_HOME/OpenKM.xml  
  
EXPOSE 8080  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
VOLUME $TOMCAT_HOME/repository  
  
# prepare Postgres usage  
RUN sed -i
's/hibernate.dialect=.*/hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect/'
$TOMCAT_HOME/OpenKM.cfg  
  
# Add the run-script  
ADD run-script.sh $TOMCAT_HOME/run-script.sh  
  
CMD $TOMCAT_HOME/run-script.sh  
  

