FROM codenvy/shellinabox  
  
RUN cd ~ && \  
sudo mkdir /usr/lib/jvm && \  
sudo wget -q -P ~/ --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u73-b02/jdk-8u73-linux-x64.tar.gz && \  
sudo tar -zxf jdk-8u73-linux-x64.tar.gz -C /usr/lib/jvm && \  
sudo update-alternatives --install /usr/bin/java java
/usr/lib/jvm/jdk1.8.0_73/bin/java 100 && \  
sudo update-alternatives --install /usr/bin/javac javac
/usr/lib/jvm/jdk1.8.0_73/bin/javac 100  
  
ENV CODENVY_APP_PORT_8080_HTTP 8080  
  
ENV WILDFLY_VERSION 10.0.0.Final  
  
USER root  
  
RUN chown -R user:user /home/user  
  
USER user  
  
RUN cd ~ && \  
wget -q
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
&& \  
tar -zxf wildfly-$WILDFLY_VERSION.tar.gz && \  
mv ~/wildfly-$WILDFLY_VERSION ~/wildfly  
  
EXPOSE 8080  
  
RUN cd ~ && \  
sudo rm -rf *.tar.gz  
  
WORKDIR /home/user  
  
CMD sh ~/wildfly/bin/standalone.sh -b 0.0.0.0 && \  
touch ~/wildfly/standalone/deployments/ROOT.war.dodeploy && \  
tail -f ~/wildfly/standalone/log/server.log

