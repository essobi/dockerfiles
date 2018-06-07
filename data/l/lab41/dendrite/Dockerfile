FROM lab41/dendrite-ungit  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
# install jq for parsing json  
RUN wget http://stedolan.github.io/jq/download/linux64/jq  
RUN chmod +x ./jq  
RUN cp jq /usr/bin  
  
# add rsyslog  
RUN sed 's/#\$ModLoad imudp/\$ModLoad imudp/' -i /etc/rsyslog.conf  
RUN sed 's/#\$UDPServerRun 514/\$UDPServerRun 514/' -i /etc/rsyslog.conf  
RUN sed 's/\$PrivDropToUser syslog/#\$PrivDropToUser syslog/' -i
/etc/rsyslog.conf  
RUN sed 's/\$PrivDropToGroup syslog/#\$PrivDropToGroup syslog/' -i
/etc/rsyslog.conf  
ADD rsyslog.conf /etc/supervisor/conf.d/rsyslog.conf  
  
ADD startup.sh /startup.sh  
RUN ln -s /usr/bin/hadoop /bin/hadoop  
  
ENV MAVEN_OPTS -Xmx2048m -XX:MaxPermSize=128m  
WORKDIR /Dendrite  
  
RUN mvn -Dmaven.repo.local=/root/lib dependency:go-offline -DskipTests=true
-DwithGitHistoryServer=true  
RUN mvn -Dmaven.repo.local=/root/lib install -DskipTests=true
-DwithGitHistoryServer=true  
RUN mvn -Dmaven.repo.local=/root/lib -o install -DskipTests=true
-DwithGitHistoryServer=true  
ADD prebuild.sh /prebuild.sh  
RUN /prebuild.sh  
  
EXPOSE 8000 8448  
# run supervisord daemon  
CMD pwd; \  
printf "*.*\t@$REMOTE_HOST" >> /etc/rsyslog.d/50-default.conf; \  
/usr/bin/supervisord; \  
sleep 2; \  
logger started dendrite container $PARENT_HOST; \  
/startup.sh; \  
mvn -o -Dmaven.repo.local=/root/lib tomcat7:run -Dmaven.tomcat.port=8000
-Dspring.profiles.active=prod -DwithGitHistoryServer=true
-Djava.security.egd=file:/dev/./urandom -DskipTests  

