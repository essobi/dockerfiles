FROM tomcat:8.0-jre8  
  
ENV KJWIKIGDOCKER_VERSION build-target  
ENV KJWIKIGDOCKER_VERSION latest  
ENV KJWIKIGDOCKER_VERSION stable  
ENV KJWIKIGDOCKER_VERSION build419  
ENV KJWIKIGDOCKER_IMAGE kjwikigdocker  
  
COPY ./kjwikigdocker.war /usr/local/tomcat/webapps/kjwikigdocker.war  
  
RUN apt-get clean  
RUN gpg --keyserver keyserver.ubuntu.com --recv-keys 8B48AD6246925553  
RUN apt-get update  
RUN apt-get install -y apt-utils --allow-unauthenticated  
RUN apt-get -y upgrade --allow-unauthenticated  
  
RUN apt-get install -y locales  
RUN locale-gen ja_JP.UTF-8  
RUN localedef -f UTF-8 -i ja_JP ja_JP  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:jp  
ENV LC_ALL ja_JP.UTF-8  
# top, ps  
# RUN apt-get install -y procps  
# for volume  
RUN mkdir -p /var/lib/kjwikigdocker  
  
# remove tomcat default contents  
RUN rm -rf /usr/local/tomcat/webapps/docs /usr/local/tomcat/webapps/examples
/usr/local/tomcat/webapps/host-manager /usr/local/tomcat/webapps/manager  
RUN rm -rf /usr/local/tomcat/webapps/ROOT/*  
  
# install default index page  
COPY index.jsp /usr/local/tomcat/webapps/ROOT/  
  
# log to stderr/stdout  
RUN cp -p /usr/local/tomcat/conf/logging.properties
/usr/local/tomcat/conf/logging.properties.orig  
COPY logging.properties /usr/local/tomcat/conf/logging.properties  
  
# log to stderr/stdout  
RUN cp -p /usr/local/tomcat/conf/server.xml
/usr/local/tomcat/conf/server.xml.orig  
COPY server.xml /usr/local/tomcat/conf/server.xml  
  
EXPOSE 8080  
VOLUME /var/lib/kjwikigdocker  
  
CMD ["catalina.sh", "run"]  

