FROM razzek/lab.java:8  
  
RUN gpg \--keyserver pool.sks-keyservers.net \--recv-keys \  
05AB33110949707C93A279E3D3EFE6B686867BA6 \  
07E48665A34DCAFAE522E5E6266191C37C037D42 \  
47309207D818FFD8DCD3F83F1931D684307A10A5 \  
541FBE7D8F78B25E055DDEE13C370389288584E7 \  
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
9BA44C2621385CB966EBA586F72C284D731FABEE \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23 \  
&& curl -fSLs "https://www.apache.org/dist/tomcat/tomcat-8/v8.0.26/bin/apache-
tomcat-8.0.26.tar.gz" -o /tmp/tomcat.tar.gz \  
&& curl -fSLs "https://www.apache.org/dist/tomcat/tomcat-8/v8.0.26/bin/apache-
tomcat-8.0.26.tar.gz.asc" -o /tmp/tomcat.tar.gz.asc \  
&& gpg \--verify /tmp/tomcat.tar.gz.asc \  
&& tar -xf /tmp/tomcat.tar.gz -C /opt \  
&& ln -s apache-tomcat-8.0.26 /opt/apache-tomcat \  
&& rm -rf /opt/apache-tomcat/bin/*.bat /tmp/tomcat.tar.gz* /opt/apache-
tomcat/work /opt/apache-tomcat/logs /opt/apache-tomcat/temp \  
&& mv /opt/apache-tomcat/conf /opt/apache-tomcat/webapps /home/service \  
&& mkdir /home/service/lib /home/service/work /home/service/logs
/home/service/temp \  
&& chown -R service:service /home/service/*  
  
ENV CATALINA_HOME=/opt/apache-tomcat CATALINA_BASE=/home/service  
  
USER service  
WORKDIR /home/service  
EXPOSE 8080 8009  
CMD [ "/opt/apache-tomcat/bin/catalina.sh", "run" ]  
  

