FROM codenvy/shellinabox  
  
RUN cd ~ && \  
sudo mkdir /usr/lib/jvm && \  
sudo wget -q -P ~/ --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u40-b25/jdk-8u40-linux-x64.tar.gz && \  
sudo tar -zxf jdk-8u40-linux-x64.tar.gz -C /usr/lib/jvm && \  
sudo update-alternatives --install /usr/bin/java java
/usr/lib/jvm/jdk1.8.0_40/bin/java 100 && \  
sudo update-alternatives --install /usr/bin/javac javac
/usr/lib/jvm/jdk1.8.0_40/bin/javac 100  
  
ENV CODENVY_APP_PORT_8080_HTTP 8080  
  
ENV WILDFLY_VERSION 8.2.0.Final  
  
RUN cd ~ && \  
sudo wget -q
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
&& \  
sudo tar -zxf wildfly-$WILDFLY_VERSION.tar.gz && \  
sudo mv ~/wildfly-$WILDFLY_VERSION ~/wildfly  
  
EXPOSE 8080  
  
RUN cd ~ && \  
sudo rm -rf *.tar.gz  
  
WORKDIR /home/user  
  
CMD sudo sh ~/wildfly/bin/standalone.sh -b 0.0.0.0 && \  
sudo touch ~/wildfly/standalone/deployments/ROOT.war.dodeploy && \  
tail -f ~/wildfly/standalone/log/server.log  
  
  

