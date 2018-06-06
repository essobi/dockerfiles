FROM tomcat:7  
RUN mkdir /usr/local/fedora  
RUN sed -i '$s,$,\nfcrepo.home=/usr/local/fedora,'
/usr/local/tomcat/conf/catalina.properties  
RUN wget -q
https://github.com/fcrepo4/fcrepo4/releases/download/fcrepo-4.1.1/fcrepo-
webapp-4.1.1.war -O /usr/local/tomcat/webapps/fcrepo.war  
RUN sed -i '$s#\\(</tomcat-users>\\)$#\n<role rolename="manager-gui"/>\n<user
username="admin" password="password" roles="manager-gui,tomcat,role1"/>\n\1#'
/usr/local/tomcat/conf/tomcat-users.xml  

