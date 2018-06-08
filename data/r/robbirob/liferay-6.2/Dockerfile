FROM eclipse/stack-base:ubuntu  
EXPOSE 4403 8000 8080 9876 22  
LABEL che:server:8080:ref=tomcat8 che:server:8080:protocol=http
che:server:8000:ref=tomcat8-debug che:server:8000:protocol=http
che:server:9876:ref=codeserver che:server:9876:protocol=http  
  
ENV MAVEN_VERSION=3.3.9 \  
TOMCAT_HOME=/home/user/tomcat8 \  
TERM=xterm  
ENV M2_HOME=/home/user/apache-maven-$MAVEN_VERSION  
ENV USER_HOME=/home/user  
ENV PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH  
  
# install liferay  
RUN cd /home/user && curl -O -s -k -L -C -
http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.2.5%20GA6/liferay-
portal-tomcat-6.2-ce-ga6-20160112152609836.zip \  
&& unzip liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip -d /home/user
\  
&& sudo rm liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip && cd -  
# add config for bdd  
RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-
properties=portal-bd-${DB_TYPE}.properties"' >> /home/user/liferay-
portal-6.2-ce-ga6/tomcat-7.0.62/bin/setenv.sh  
# add configuration liferay file  
ADD lep/portal-bundle.properties /home/user/liferay-portal-6.2-ce-ga6/portal-
bundle.properties  
ADD lep/portal-bd-MYSQL.properties /home/user/liferay-portal-6.2-ce-
ga6/portal-bd-MYSQL.properties  
#ADD lep/portal-bd-POSTGRESQL.properties /opt/liferay-portal-6.2-ce-
ga6/portal-bd-POSTGRESQL.properties  
ENV LIFERAY_HOME=/home/user/liferay-portal-6.2-ce-ga6  
  
  
# volumes  
VOLUME ["/var/liferay-home", "/home/user/liferay-portal-6.2-ce-ga6/"]  
  
RUN mkdir /home/user/tomcat8 /home/user/apache-maven-$MAVEN_VERSION && \  
wget -qO- "http://apache.ip-
connect.vn.ua/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" | tar -zx --strip-components=1 -C
/home/user/apache-maven-$MAVEN_VERSION/ && \  
echo "export MAVEN_OPTS=\$JAVA_OPTS" >> /home/user/.bashrc  

