FROM java:7  
MAINTAINER João Fidalgo <joao.fidalgo@outlook.com>  
  
RUN curl -O -s -k -L -C -
http://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.2.5%20GA6/liferay-
portal-tomcat-6.2-ce-ga6-20160112152609836.zip && \  
unzip liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip -d /opt && \  
rm liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip  
  
RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-
properties=portal-db.properties"' >> /opt/liferay-portal-6.2-ce-
ga6/tomcat-7.0.62/bin/setenv.sh  
  
ADD ./config/portal-bundle.properties /opt/liferay-portal-6.2-ce-ga6/portal-
bundle.properties  
ADD ./config/portal-db.properties /opt/liferay-portal-6.2-ce-ga6/portal-
db.properties  
  
VOLUME /var/liferay  
  
EXPOSE 8080  
ONBUILD ADD ./deploy /var/liferay/deploy  
ONBUILD ADD ./lib /var/liferay/lib  
ONBUILD COPY ./bin/*.sh /var/liferay/bin  
  
CMD ["run"]  
ENTRYPOINT ["/opt/liferay-portal-6.2-ce-ga6/tomcat-7.0.62/bin/catalina.sh"]  

