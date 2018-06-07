FROM inclusivedesign/java  
  
ADD . /tmp/rbmm-java  
  
WORKDIR /tmp/rbmm-java  
  
RUN yum -y install maven tomcat && \  
mv start.sh /usr/local/bin/start.sh && \  
chmod +x /usr/local/bin/start.sh && \  
sed -i 's/PERFORM_INTEGRATION_TESTS=true/PERFORM_INTEGRATION_TESTS=false/'
src/main/webapp/WEB-INF/config.properties && \  
mvn clean install && \  
cp target/CLOUD4All_RBMM_Restful_WS.war /usr/share/tomcat/webapps/ && \  
rm -fr /tmp/rbmm-java ~/.m2 && \  
yum -y autoremove maven && \  
yum clean all  
  
EXPOSE 8080  
CMD ["/usr/local/bin/start.sh"]  

