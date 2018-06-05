FROM sonatype/nexus3:3.7.1  
  
  
ENV LDAP_ENABLED=true \  
NEXUS_CONTEXT=nexus \  
DEBUG_LOGGING=false \  
LDAP_SEARCH_BASE="" \  
LDAP_NAME=nexusldap \  
LDAP_URL="" \  
LDAP_PORT=389 \  
LDAP_AUTH_PROTOCOL=ldap \  
LDAP_AUTH_SCHEME=simple \  
LDAP_USER_EMAIL_ATTRIBUTE=mail \  
LDAP_GROUPS_AS_ROLES=true \  
LDAP_GROUP_BASE_DN=ou=groups \  
LDAP_GROUP_ID_ATTRIBUTE=cn \  
LDAP_GROUP_MEMBER_ATTRIBUTE=uniqueMember \  
LDAP_GROUP_OBJECT_CLASS=groupOfUniqueNames \  
LDAP_PREFERRED_PASSWORD_ENCODING=crypt \  
LDAP_MAP_GROUP_AS_ROLES=true \  
LDAP_USER_ID_ATTRIBUTE=uid \  
LDAP_USER_PASSWORD_ATTRIBUTE=userPassword \  
LDAP_USER_OBJECT_CLASS=inetOrgPerson \  
LDAP_USER_BASE_DN=ou=people \  
LDAP_USER_REAL_NAME_ATTRIBUTE=cn \  
LDAP_GROUP_MEMBER_FORMAT='${dn}' \  
NEXUS_CREATE_CUSTOM_ROLES=false  
  
USER root  
  
# Install groovy  
RUN yum install -y zip unzip  
RUN yum install -y which  
RUN curl -s get.sdkman.io | bash  
RUN source "$HOME/.sdkman/bin/sdkman-init.sh"  
RUN yes | /bin/bash -l -c "sdk install groovy 2.4.15"  
  
ENV PATH="/root/.sdkman/candidates/groovy/2.4.15/bin:${PATH}"  
RUN export PATH  
  
COPY resources/nexus.sh /usr/local/bin/  
COPY resources/provision.sh /usr/local/bin/  
COPY resources/ /resources/  
COPY resources/conf/grapeConfig.xml /root/.groovy/  
  
  
RUN grape install org.sonatype.nexus nexus-rest-client 3.6.0-02 \  
&& grape install org.sonatype.nexus nexus-rest-jackson2 3.6.0-02 \  
&& grape install org.sonatype.nexus nexus-script 3.6.0-02 \  
&& grape install org.jboss.spec.javax.servlet jboss-servlet-api_3.1_spec
1.0.0.Final \  
&& grape install com.fasterxml.jackson.core jackson-core 2.8.6 \  
&& grape install com.fasterxml.jackson.core jackson-databind 2.8.6 \  
&& grape install com.fasterxml.jackson.core jackson-annotations 2.8.6 \  
&& grape install com.fasterxml.jackson.jaxrs jackson-jaxrs-json-provider 2.8.6
\  
&& grape install org.jboss.spec.javax.ws.rs jboss-jaxrs-api_2.0_spec
1.0.1.Beta1 \  
&& grape install org.jboss.spec.javax.annotation jboss-annotations-
api_1.2_spec 1.0.0.Final \  
&& grape install javax.activation activation 1.1.1 \  
&& grape install net.jcip jcip-annotations 1.0 \  
&& grape install org.jboss.logging jboss-logging-annotations 2.0.1.Final \  
&& grape install org.jboss.logging jboss-logging-processor 2.0.1.Final \  
&& grape install com.sun.xml.bind jaxb-impl 2.2.7 \  
&& grape install com.sun.mail javax.mail 1.5.6 \  
&& grape install org.apache.james apache-mime4j 0.6  
  
RUN chmod u+x /usr/local/bin/nexus.sh && chmod u+x /usr/local/bin/provision.sh  
  
ENTRYPOINT ["/usr/local/bin/nexus.sh"]  

