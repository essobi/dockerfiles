FROM anduin/anduin-common:1.0  
MAINTAINER ductamnguyen@anduintransact.com  
  
ENV KEYCLOAK_VERSION 3.4.1.Final  
# Enables signals getting passed from startup script to JVM  
# ensuring clean shutdown when container is stopped.  
ENV LAUNCH_JBOSS_IN_BACKGROUND 1  
ENV PROXY_ADDRESS_FORWARDING true  
  
RUN apt-get -y update && apt-get install -y jq && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -O /opt/keycloak-${KEYCLOAK_VERSION}.tar.gz
https://downloads.jboss.org/keycloak/${KEYCLOAK_VERSION}/keycloak-${KEYCLOAK_VERSION}.tar.gz
&& \  
cd /opt && \  
tar xvzf keycloak-${KEYCLOAK_VERSION}.tar.gz && \  
mv keycloak-${KEYCLOAK_VERSION} keycloak && \  
rm keycloak-${KEYCLOAK_VERSION}.tar.gz  
  
ADD cli /opt/keycloak/cli  
RUN cd /opt/keycloak && bin/jboss-cli.sh --file=cli/standalone-
configuration.cli && \  
cd /opt/keycloak && bin/jboss-cli.sh --file=cli/databases/postgres/standalone-
configuration.cli && \  
rm -rf /opt/keycloak/standalone/configuration/standalone_xml_history  
  
ENV JDBC_POSTGRES_VERSION 42.1.4  
RUN mkdir -p
/opt/keycloak/modules/system/layers/base/org/postgresql/jdbc/main; cd
/opt/keycloak/modules/system/layers/base/org/postgresql/jdbc/main; curl -L
http://central.maven.org/maven2/org/postgresql/postgresql/$JDBC_POSTGRES_VERSION/postgresql-$JDBC_POSTGRES_VERSION.jar
> postgres-jdbc.jar  
ADD databases/postgres/module.xml
/opt/keycloak/modules/system/layers/base/org/postgresql/jdbc/main  
  
RUN locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
ENV VAULT_VERSION=0.8.3  
RUN apt-get -y update && apt-get install -y jq unzip && \  
wget
https://releases.hashicorp.com/vault/$VAULT_VERSION/vault_${VAULT_VERSION}_linux_amd64.zip
&& \  
unzip vault_${VAULT_VERSION}_linux_amd64.zip && \  
mv vault /usr/bin && \  
rm vault_${VAULT_VERSION}_linux_amd64.zip && \  
wget
https://raw.githubusercontent.com/anduintransaction/Dockerfiles/master/vault-
kube/vault-kube && \  
mv vault-kube /usr/bin && \  
chmod 755 /usr/bin/vault-kube && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
ADD run-keycloak.sh /opt/keycloak/bin/run-keycloak.sh  
ADD entrypoint.sh /opt/entrypoint.sh  
  
EXPOSE 8080  
ENTRYPOINT [ "/opt/entrypoint.sh" ]  
  
CMD [ "server" ]  

