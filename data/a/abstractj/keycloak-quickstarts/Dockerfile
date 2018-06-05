FROM jboss/wildfly  
  
ENV MAVEN_VERSION 3.3.9  
ENV KEYCLOAK_VERSION 3.4.3.Final  
  
# Set the repository  
ENV REPO_NAME keycloak-quickstarts  
  
USER root  
  
# Install Git  
RUN yum install -q -y git && yum -q clean all  
  
# Install Maven  
RUN curl -fsSL
https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
USER jboss  
  
RUN echo 'alias deploy="mvn clean wildfly:deploy -DskipTests=true
-Denforcer.skip=true"' >> $HOME/.bashrc  
RUN mkdir -p /opt/jboss/.m2  
  
ADD config/adapter-install-saml-offline.cli $JBOSS_HOME/bin  
  
# Clone repository  
RUN git clone https://github.com/keycloak/$REPO_NAME.git  
  
# Install WildFly adapter  
RUN curl -fsSL
https://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/adapters/keycloak-
oidc/keycloak-wildfly-adapter-dist-$KEYCLOAK_VERSION.tar.gz | tar xzf - -C
/opt/jboss/wildfly \  
&& $JBOSS_HOME/bin/jboss-cli.sh --file=$JBOSS_HOME/bin/adapter-install-
offline.cli  
  
RUN curl -fsSL
https://downloads.jboss.org/keycloak/3.4.3.Final/adapters/saml/keycloak-saml-
wildfly-adapter-dist-3.4.3.Final.tar.gz | tar xzf - -C /opt/jboss/wildfly \  
&& $JBOSS_HOME/bin/jboss-cli.sh --file=$JBOSS_HOME/bin/adapter-install-saml-
offline.cli  
  

