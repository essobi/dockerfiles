FROM rsippl/centos-jdk  
  
MAINTAINER Ralf Sippl <ralf.sippl@gmail.com>  
  
RUN yum update -y  
RUN yum install -y epel-release  
RUN yum install -y \  
unzip \  
supervisor  
RUN yum clean all  
  
RUN curl -O -k -L
http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/7.0.0%20GA1/liferay-
portal-tomcat-7.0-ce-ga1-20160331161017956.zip \  
&& unzip liferay-portal-tomcat-7.0-ce-ga1-20160331161017956.zip -d /opt \  
&& rm liferay-portal-tomcat-7.0-ce-ga1-20160331161017956.zip  
RUN ln -s /opt/liferay-portal-7.0-ce-ga1 /opt/liferay \  
&& ln -s /opt/liferay/tomcat-8.0.32 /opt/liferay/tomcat  
RUN echo -e '\nCATALINA_OPTS="$CATALINA_OPTS
-Djava.security.egd=file:/dev/./urandom"' >> /opt/liferay/tomcat/bin/setenv.sh  
  
COPY assets/supervisord.conf /etc/supervisord.conf  
COPY assets/init.sh /opt/liferay/init.sh  
  
VOLUME ["/opt/liferay"]  
  
EXPOSE 8080  
CMD /usr/bin/supervisord -n  

