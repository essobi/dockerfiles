FROM quin/oraclejava8  
MAINTAINER quin  
  
ENV CATALINA_HOME /usr/share/tomcat  
ENV CATALINA_BASE /var/lib/tomcat  
  
ADD ansible /srv/ansible  
WORKDIR /srv/ansible  
RUN ansible-playbook site.yml -c local  
  
EXPOSE 8080  
WORKDIR /var/lib/tomcat  
ENTRYPOINT ["/usr/share/tomcat/bin/catalina.sh", "run"]  

