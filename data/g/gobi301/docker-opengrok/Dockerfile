FROM tomcat:8.0  
RUN mkdir /src  
RUN mkdir /data  
RUN ln -s /data /var/opengrok  
RUN ln -s /src /var/opengrok/src  
RUN wget
"https://github.com/OpenGrok/OpenGrok/files/467358/opengrok-0.12.1.6.tar.gz.zip"
-O /tmp/opengrok-0.12.1.6.tar.gz.zip  
RUN wget "http://ftp.us.debian.org/debian/pool/main/e/exuberant-
ctags/exuberant-ctags_5.9~svn20110310-11_amd64.deb" -O /tmp/exuberant-
ctags_5.9-svn20110310-11_amd64.deb  
RUN unzip /tmp/opengrok-0.12.1.6.tar.gz.zip -d /tmp  
RUN tar zxvf /tmp/opengrok-0.12.1.6.tar.gz -C /  
RUN dpkg -i /tmp/exuberant-ctags_5.9-svn20110310-11_amd64.deb  
  
ENV SRC_ROOT /src  
ENV OPENGROK_TOMCAT_BASE /usr/local/tomcat  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
ENV PATH /opengrok-0.12.1.6/bin:$PATH  
  
ENV CATALINA_BASE /usr/local/tomcat  
ENV CATALINA_HOME /usr/local/tomcat  
ENV CATALINA_TMPDIR /usr/local/tomcat/temp  
ENV JRE_HOME /usr  
ENV CLASSPATH
/usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar  
  
RUN apt-get update && apt-get install -y \  
git \  
mercurial  
  
WORKDIR $CATALINA_HOME  
RUN /opengrok-0.12.1.6/bin/OpenGrok deploy  
  
EXPOSE 8080  
ADD scripts /scripts  
CMD ["/scripts/start.sh"]  

