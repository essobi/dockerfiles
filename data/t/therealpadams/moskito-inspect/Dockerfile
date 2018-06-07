FROM tomcat:alpine  
  
MAINTAINER Paul Adams <paul@baggerspion.net>  
  
ENV MOSKITO_VERSION 2.7.8  
  
RUN wget -q -O moskito.tgz
http://www.moskito.org/download/moskito-$MOSKITO_VERSION.tgz \  
&& tar zxf moskito.tgz \  
&& rm -rf $CATALINA_HOME/webapps/* \  
&& mv moskito/moskito-inspect/moskito-inspect-standalone-$MOSKITO_VERSION.war
$CATALINA_HOME/webapps/ROOT.war \  
&& rm -rf moksito.tgz moskito/

