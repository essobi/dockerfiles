FROM quintenk/jdk7-oracle  
MAINTAINER Stefan Armbruster <stefan@armbruster-it.de>  
# make sure the package repository is up to date  
  
RUN update-java-alternatives -s java-7-oracle  
RUN apt-get update && apt-get -y install tomcat7 git-core curl  
  
# set JAVA_HOME for tomcat to oracle jdk 7  
RUN sed -i -e 's/#\\(JAVA_HOME\\)=\\(.*\\)\/.*$/\1=\2\/java-7-oracle/'
/etc/default/tomcat7  
  
# web rabbithole and place it under context /console  
RUN curl -L -o /var/lib/tomcat7/webapps/console.war
"http://dl.bintray.com/sarmbruster/generic/rabbithole-2.0.0-RC1.war"  
# place graphgists in root context  
RUN rm -rf /var/lib/tomcat7/webapps/ROOT  
RUN git clone https://github.com/neo4j-contrib/graphgist.git
/var/lib/tomcat7/webapps/ROOT  
# adopt CONSOLE_URL_BASE to point to locally installed rabbithole  
RUN sed -i -e "s/\\(var CONSOLE_URL_BASE =\\).*/\1 '\/console';/"
/var/lib/tomcat7/webapps/ROOT/js/console.js;  
# fire tomcat up  
CMD service tomcat7 start && tail -f /var/log/tomcat7/catalina.out  
EXPOSE 8080

