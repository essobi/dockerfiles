FROM rangalo/java8  
  
MAINTAINER rangalo "hard.mehta@gmail.com"  
RUN wget -q --no-cookies --no-check
http://download.jboss.org/wildfly/10.1.0.Final/wildfly-10.1.0.Final.zip && \  
mkdir /opt/redhat && \  
mv -v wildfly-10.1.0.Final.zip /opt/redhat && \  
cd /opt/redhat && \  
unzip -q wildfly-10.1.0.Final.zip && \  
ln -svn /opt/redhat/wildfly-10.1.0.Final /opt/redhat/wildfly && \  
rm -f /opt/redhat/wildfly-10.1.0.Final.zip && \  
echo "JBOSS_HOME=/opt/redhat/wildfly"  
ENV JBOSS_HOME /opt/redhat/wildfly  
ENV PATH $JBOSS_HOME/bin:$PATH  
  
ADD run.sh /run.sh  
  
RUN chmod +x run.sh  
  
# 9990 (administration), 8080 (HTTP listener), 8181 (HTTPS listener)  
EXPOSE 9990 8080 8181  
CMD ["/run.sh"]  

