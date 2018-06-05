FROM adelton/freeipa-client:latest  
  
ADD scripts/ /opt/jboss/scripts/  
ADD pam.d/keycloak /etc/pam.d/keycloak  
ADD dist/libunix*.rpm /opt/jboss/rpm/  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0  
RUN dnf install -y iputils freeipa-admintools java-1.8.0-openjdk* sssd-dbus
nmap-ncat pamtester bash-completion libsss_simpleifp maven zsh && dnf clean
all  
  
RUN mkdir /var/run/dbus  
RUN mkdir -p /opt/jboss/keycloak-repo  
RUN chmod -v +x /opt/jboss/scripts/*  
RUN chown 1000:1000 -Rv /opt/jboss/keycloak-repo  
WORKDIR /opt/jboss/keycloak-repo  
  

