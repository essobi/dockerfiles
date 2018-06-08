FROM ubuntu:latest  
  
MAINTAINER mcsaky <mihai.csaky@sysop-consulting.ro>  
  
# Set the debconf frontend to Noninteractive  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
ENV JAVA_HOME /usr/local/java  
ENV ORACLE_JAVA_HOME /usr/lib/jvm/java-8-oracle/  
ENV WEBAPP_VERSION=tomcat-8.0.32  
ENV PORTAL_VERSION=liferay-portal-7.0-ce-ga1  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get -y install software-properties-common  
  
#prepare and install JDK  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
  
RUN ln -s $ORACLE_JAVA_HOME $JAVA_HOME  
  
#install additional software  
RUN apt-get -y install ant curl unzip sudo tar software-properties-common
python-jinja2 python-pip jq git  
RUN pip install j2cli  
  
#
http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/7.0.0%20GA1/liferay-
portal-wildfly-7.0-ce-ga1-20160331161017956.zip  
#
http://netix.dl.sourceforge.net/project/lportal/Liferay%20Portal/7.0.0%20GA1/liferay-
portal-tomcat-7.0-ce-ga1-20160331161017956.zip  
# install liferay  
RUN curl -O -s -k -L -C -
http://netix.dl.sourceforge.net/project/lportal/Liferay%20Portal/7.0.0%20GA1/liferay-
portal-tomcat-7.0-ce-ga1-20160331161017956.zip \  
&& unzip liferay-portal-tomcat-7.0-ce-ga1-20160331161017956.zip -d /opt \  
&& rm liferay-portal-tomcat-7.0-ce-ga1-20160331161017956.zip  
  
# add config for database  
RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-
properties=portal-db-MYSQL.properties"' >>
/opt/$PORTAL_VERSION/$WEBAPP_VERSION/bin/setenv.sh  
  
# add configuration liferay file  
ADD conf/portal-bundle.properties /opt/$PORTAL_VERSION/portal-
bundle.properties  
ADD conf/portal-db-MYSQL.properties.j2 /opt/$PORTAL_VERSION/portal-db-
MYSQL.properties.j2  
ADD run.sh /opt/  
  
# volumes  
VOLUME ["/opt/liferay-home", "/opt/$PORTAL_VERSION"]  
  
# Ports  
EXPOSE 8080  
#RUN useradd -d /opt/liferay-home -s /bin/bash liferay  
#RUN chown -R liferay:liferay /opt/;  
RUN chmod 755 /opt/run.sh  
#USER liferay  
RUN apt-get clean all  
  
# EXEC  
ENTRYPOINT ["/opt/run.sh"]  

