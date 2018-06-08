FROM stackbrew/ubuntu:12.04  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
RUN (echo "deb http://archive.ubuntu.com/ubuntu/ precise main restricted
universe multiverse" > /etc/apt/sources.list && echo "deb
http://archive.ubuntu.com/ubuntu/ precise-updates main restricted universe
multiverse" >> /etc/apt/sources.list && echo "deb
http://archive.ubuntu.com/ubuntu/ precise-backports main restricted universe
multiverse" >> /etc/apt/sources.list && echo "deb
http://archive.ubuntu.com/ubuntu/ precise-security main restricted universe
multiverse" >> /etc/apt/sources.list)  
RUN apt-get update  
  
# set environment variables  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV PATH $PATH:$HOME/bin:$JAVA_HOME/bin  
  
# install prereqs  
RUN apt-get install -y build-essential nano sudo wget  
  
# install oracle jdk  
RUN (wget --progress=dot --no-check-certificate -O /tmp/server-
jre-7u65-linux-x64.tar.gz --header "Cookie: oraclelicense=a"
http://download.oracle.com/otn-pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.tar.gz
&&\  
echo "c223bdbaf706f986f7a5061a204f641f /tmp/server-jre-7u65-linux-x64.tar.gz"
| md5sum -c > /dev/null 2>&1 || echo "ERROR: MD5SUM MISMATCH" &&\  
tar xzf /tmp/server-jre-7u65-linux-x64.tar.gz &&\  
mkdir -p /usr/lib/jvm/java-7-oracle &&\  
mv jdk1.7.0_65/* /usr/lib/jvm/java-7-oracle/ &&\  
rm -rf jdk1.7.0_65 && rm /tmp/server-jre-7u65-linux-x64.tar.gz &&\  
chown root:root -R /usr/lib/jvm/java-7-oracle &&\  
update-alternatives --install /usr/bin/java java
/usr/lib/jvm/java-7-oracle/jre/bin/java 1 && update-alternatives \--set java
/usr/lib/jvm/java-7-oracle/jre/bin/java &&\  
update-alternatives --install /usr/bin/javac javac
/usr/lib/jvm/java-7-oracle/bin/javac 1 && update-alternatives \--set javac
/usr/lib/jvm/java-7-oracle/bin/javac)  
# create profile for java  
RUN (echo 'export JAVA_HOME=/usr/lib/jvm/java-7-oracle' >
/etc/profile.d/java.sh &&\  
echo 'export PATH=$PATH:$HOME/bin:$JAVA_HOME/bin' >> /etc/profile.d/java.sh)  
  
# compile postgres  
RUN (mkdir -p /opt/postgresql &&\  
chown root:root /opt/postgresql &&\  
wget http://ftp.postgresql.org/pub/source/v8.4.15/postgresql-8.4.15.tar.gz -O
/opt/postgresql/postgresql-8.4.15.tar.gz &&\  
cd /opt/postgresql &&\  
gunzip postgresql-8.4.15.tar.gz &&\  
tar xvf postgresql-8.4.15.tar &&\  
rm postgresql-8.4.15.tar &&\  
mkdir -p /opt/postgresql/8.4.15 &&\  
cd /opt/postgresql/postgresql-8.4.15/ &&\  
apt-get install -y libreadline-dev &&\  
apt-get install -y zlib1g-dev &&\  
./configure exec_prefix=/opt/postgresql/8.4.15 &&\  
make exec_prefix=/opt/postgresql/8.4.15 &&\  
make install exec_prefix=/opt/postgresql/8.4.15)  
  
# add postgres required directories  
RUN (mkdir /opt/postgresql/8.4.15/data /opt/postgresql/8.4.15/log
/home/postgres &&\  
useradd -s /bin/bash postgres &&\  
chown -R postgres:postgres /opt/postgresql &&\  
chown -R postgres:postgres /home/postgres)  
  
# create environment file  
RUN (echo 'export POSTGRES_VERSION=8.4.15' >
/home/postgres/.environment-8.4.15 &&\  
echo 'export LD_LIBRARY_PATH=/opt/postgres/${POSTGRES_VERSION}/lib' >>
/home/postgres/.environment-8.4.15 &&\  
echo 'export PATH=/opt/postgres/${POSTGRES_VERSION}/bin:${PATH}' >>
/home/postgres/.environment-8.4.15 && \  
chown postgres:postgres /home/postgres/.environment-8.4.15)  
  
# create environment file for postgres  
RUN su - postgres -c ". .environment-8.4.15 &&
/opt/postgresql/8.4.15/bin/initdb -D /opt/postgresql/8.4.15/data/
--encoding=UNICODE"  
# add files  
ADD postgresql-8.4.15 /home/postgres/postgresql-8.4.15  
ADD postgresql.8.4.15 /etc/init.d/postgresql.8.4.15  
ADD commands1.sql /home/postgres/commands1.sql  
ADD commands2.sql /home/postgres/commands2.sql  
RUN (chown -R postgres:postgres /home/postgres &&\  
chmod 777 /home/postgres/postgresql-8.4.15 &&\  
chmod 777 /etc/init.d/postgresql.8.4.15)  
  
# start postgres and run commands  
RUN (su - postgres -c ". .environment-8.4.15 &&
/home/postgres/postgresql-8.4.15 start && sleep 5 &&\  
/opt/postgresql/8.4.15/bin/psql -f /home/postgres/commands1.sql &&\  
/opt/postgresql/8.4.15/bin/psql -h localhost -U liferay -d lportal -f
/home/postgres/commands2.sql &&\  
/home/postgres/postgresql-8.4.15 stop")  
  
# postgres configuration  
RUN echo 'host all all 0.0.0.0/0 md5' >>
/opt/postgresql/8.4.15/data/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /opt/postgresql/8.4.15/data/postgresql.conf  
  
# install tomcat  
RUN (mkdir /opt/liferay && \  
sudo chown root:root /opt/liferay &&\  
wget http://mirror.cogentco.com/pub/apache/tomcat/tomcat-7/v7.0.56/bin/apache-
tomcat-7.0.56.tar.gz -O /opt/liferay/apache-tomcat-7.0.56.tar.gz && \  
cd /opt/liferay && \  
tar xvf apache-tomcat-7.0.56.tar.gz && \  
rm /opt/liferay/apache-tomcat-7.0.56.tar.gz && \  
mv apache-tomcat-7.0.56 tomcat)  
  
# liferay setup  
RUN (apt-get install -y unzip &&\  
mkdir /opt/liferay/tomcat/lib/ext &&\  
cd /opt/liferay/tomcat/lib/ext &&\  
wget
http://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.1.1%20GA2/liferay-
portal-dependencies-6.1.1-ce-ga2-20120731132656558.zip/download -O
/opt/liferay/tomcat/lib/ext/liferay-portal-dependencies-6.1.1-ce-
ga2-20120731132656558.zip &&\  
unzip liferay-portal-dependencies-6.1.1-ce-ga2-20120731132656558.zip &&\  
rm liferay-portal-dependencies-6.1.1-ce-ga2-20120731132656558.zip &&\  
mv liferay-portal-dependencies-6.1.1-ce-ga2/*.jar . && \  
rm -rf liferay-portal-dependencies-6.1.1-ce-ga2)  
  
RUN (wget
http://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.1.1%20GA2/liferay-
portal-src-6.1.1-ce-ga2-20120731132656558.zip/download -O /tmp/liferay-portal-
src-6.1.1-ce-ga2-20120731132656558.zip &&\  
cd /tmp && unzip /tmp/liferay-portal-src-6.1.1-ce-ga2-20120731132656558.zip
&&\  
rm /tmp/liferay-portal-src-6.1.1-ce-ga2-20120731132656558.zip && \  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/development/activation.jar
/opt/liferay/tomcat/lib/ext/ &&\  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/development/jms.jar
/opt/liferay/tomcat/lib/ext/ &&\  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/development/jta.jar
/opt/liferay/tomcat/lib/ext/ &&\  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/development/jutf7.jar
/opt/liferay/tomcat/lib/ext/ &&\  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/development/mail.jar
/opt/liferay/tomcat/lib/ext/ &&\  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/development/persistence.jar
/opt/liferay/tomcat/lib/ext/ &&\  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/portal/ccpp.jar
/opt/liferay/tomcat/lib/ext/)  
  
RUN (mkdir -p
/opt/liferay/tomcat/temp/liferay/com/liferay/portal/deploy/dependencies && \  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/development/resin.jar
/opt/liferay/tomcat/temp/liferay/com/liferay/portal/deploy/dependencies/ &&\  
cp /tmp/liferay-portal-src-6.1.1-ce-ga2/lib/development/script-10.jar
/opt/liferay/tomcat/temp/liferay/com/liferay/portal/deploy/dependencies/)  
# install ODBC driver  
RUN wget http://jdbc.postgresql.org/download/postgresql-8.4-703.jdbc4.jar -O
/opt/liferay/tomcat/lib/ext/postgresql-8.4-703.jdbc4.jar  
  
# install jra.jar  
RUN (wget http://www.java2s.com/Code/JarDownload/jta/jta-1.3.1.jar.zip -O
/tmp/jta-1.3.1.jar.zip &&\  
cd /tmp && unzip jta-1.3.1.jar.zip && rm jta-1.3.1.jar.zip &&\  
mv jta-1.3.1.jar /opt/liferay/tomcat/lib/ext/)  
# add setenv.sh  
ADD setenv.sh /opt/liferay/tomcat/bin/setenv.sh  
  
# add ROOT.xml  
RUN mkdir -p /opt/liferay/tomcat/conf/Catalina/localhost  
ADD ROOT.xml /opt/liferay/tomcat/conf/Catalina/localhost/ROOT.xml  
  
# patch files  
ADD catalina.properties.patch /tmp/catalina.properties.patch  
RUN (patch /opt/liferay/tomcat/conf/catalina.properties <
/tmp/catalina.properties.patch &&\  
rm /tmp/catalina.properties.patch)  
ADD server.xml.patch /tmp/server.xml.patch  
RUN (patch /opt/liferay/tomcat/conf/server.xml < /tmp/server.xml.patch &&\  
rm /tmp/server.xml.patch)  
  
# cleanup default tomcat  
RUN (rm -rf /opt/liferay/tomcat/webapps/ROOT/* &&\  
wget
http://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.1.1%20GA2/liferay-
portal-6.1.1-ce-ga2-20120731132656558.war/download -O
/opt/liferay/tomcat/webapps/ROOT/liferay-portal-6.1.1-ce-
ga2-20120731132656558.war &&\  
cd /opt/liferay/tomcat/webapps/ROOT && jar -xf liferay-portal-6.1.1-ce-
ga2-20120731132656558.war &&\  
rm liferay-portal-6.1.1-ce-ga2-20120731132656558.war)  
  
ADD portal-ext.properties /opt/liferay/tomcat/webapps/ROOT/WEB-
INF/classes/portal-ext.properties  
ADD portal-setup-wizard.properties /opt/liferay/portal-setup-wizard.properties  
  
######################  
# add run file  
ADD run /usr/local/bin/run  
  
EXPOSE 8080  
EXPOSE 5432  
  
CMD ["/usr/local/bin/run"]  

