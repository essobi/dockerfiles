FROM glassfish:4.1-jdk8  
  
RUN echo "AS_ADMIN_PASSWORD=" > /tmp/pass  
RUN echo "AS_ADMIN_NEWPASSWORD=admin" >> /tmp/pass  
RUN /usr/local/glassfish4/bin/asadmin --user admin --passwordfile /tmp/pass
change-admin-password --domain_name domain1  
RUN mkdir /home/glassfish  
  
VOLUME /home/glassfish  
  
CMD asadmin start-domain --verbose  

