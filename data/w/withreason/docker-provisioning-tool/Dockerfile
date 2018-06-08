FROM centos:7.1.1503  
MAINTAINER "Reason" <hello@withreason.co.uk>  
  
WORKDIR /tmp  
  
#Required environment variables:  
ENV container docker  
ENV TERM=xterm  
ENV JAVA_HOME /usr/java/jdk1.8.0_71  
ENV PATH=$JAVA_HOME/bin:$JAVA_HOME/jre:$PATH  
ENV CATALINA_HOME /opt/tomcat  
ENV CATALINA_BASE /opt/tomcat  
ENV CATALINA_OPTS="-server -Xms1024m -Xmx1024m -XX:MaxPermSize=256m"  
#Optional aliases:  
RUN echo "alias j='ps -ef | grep java'" >> ~/.bashrc  
RUN echo "alias gotom='cd /opt/tomcat'" >> ~/.bashrc  
RUN echo "alias tomtail='tail -300f /opt/tomcat/logs/appengine.log'" >>
~/.bashrc  
RUN echo "alias tomstop='/opt/tomcat/bin/shutdown.sh'" >> ~/.bashrc  
RUN echo "alias tomstart='/opt/tomcat/bin/startup.sh'" >> ~/.bashrc  
RUN echo "alias tomclean='rm -Rf /opt/tomcat/logs/*'" >> ~/.bashrc  
RUN echo "alias bounce='tomstop; tomclean; tomstart; tomtail'" >> ~/.bashrc  
  
#Required tools:  
#Required apps (download and verify):  
RUN yum install -y tar  
  
#Java  
ADD ./install/common/jdk-8u71-linux-x64.rpm jdk-8u71-linux-x64.rpm  
RUN rpm -ivh jdk-8u71-linux-x64.rpm  
RUN update-alternatives --install /usr/bin/java java
/usr/java/jdk1.8.0_71/bin/java 0  
RUN update-alternatives --set java /usr/java/jdk1.8.0_71/bin/java  
  
#tomcat (install)  
RUN groupadd tomcat  
RUN mkdir /opt/tomcat  
RUN useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat  
COPY ./install/tomcat/apache-tomcat-8.0.32.tar.gz /tmp  
RUN tar xvf apache-tomcat-8.0.32.tar.gz -C /opt/tomcat --strip-components=1  
  
#(configure)  
WORKDIR /opt/tomcat  
RUN chgrp -R tomcat conf  
RUN chmod g+rwx conf  
RUN chmod g+r conf/*  
RUN chown -R tomcat work/ temp/ logs/  
ADD ./config/tomcat-users.xml /opt/tomcat/conf/tomcat-users.xml  
ADD ./config/ROOT.xml /opt/tomcat/conf/Catalina/localhost/ROOT.xml  
ADD ./config/appengine.properties
/opt/tomcat/conf/Catalina/localhost/appengine.properties  
RUN ln -s /usr/share/java native  
ADD ./config/logging.properties /opt/tomcat/conf/logging.properties  
RUN chown -R tomcat:tomcat /opt/tomcat  
  
#cleanup  
WORKDIR /tmp  
RUN rm -Rf /tmp/*  
  
#Specify initialisation scripts  
ADD ./init.sh /init.sh  
RUN chmod 755 /init.sh  
CMD ["/bin/bash", "/init.sh"]  

