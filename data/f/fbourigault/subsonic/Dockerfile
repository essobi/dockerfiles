FROM tomcat:8-jre8  
  
RUN apt-get update && apt-get -y install -f libav-tools lame && rm -r
/var/lib/apt/lists/*  
  
RUN rm -r $CATALINA_HOME/webapps/*  
  
ENV SUBSONIC_VERSION 5.3  
RUN curl -L
https://github.com/EugeneKay/subsonic/releases/download/v$SUBSONIC_VERSION-
kang/subsonic-v$SUBSONIC_VERSION-kang.war -o $CATALINA_HOME/webapps/ROOT.war  

