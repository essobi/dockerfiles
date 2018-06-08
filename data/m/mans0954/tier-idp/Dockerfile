FROM tomcat  
MAINTAINER Christopher Hoskin "christopher.hoskin@gmail.com"  
# Based on https://github.com/Internet2/tier-idp/  
# Original Copyright and License unknown  
# Modifications Copyright Christopher Hoskin  
# Original Maintainer Mark McCahill "mark.mccahill@duke.edu"  
USER root  
ENV version=3.3.1  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y wget unzip  
  
RUN cd /opt  
  
#  
# Shibboleth IDP  
#  
RUN set -e ; \  
mkdir /usr/local/dist ; \  
cd /usr/local/dist ; \  
wget http://shibboleth.net/downloads/identity-provider/${version}/shibboleth-
identity-provider-${version}.tar.gz ; \  
wget http://shibboleth.net/downloads/identity-provider/${version}/shibboleth-
identity-provider-${version}.tar.gz.asc ; \  
wget http://shibboleth.net/downloads/identity-provider/${version}/shibboleth-
identity-provider-${version}.tar.gz.sha256 ; \  
wget https://shibboleth.net/downloads/PGP_KEYS ; \  
gpg --import PGP_KEYS ; \  
sha256sum --check shibboleth-identity-provider-${version}.tar.gz.sha256 ; \  
gpg shibboleth-identity-provider-${version}.tar.gz.asc ; \  
tar -xvzf shibboleth-identity-provider-${version}.tar.gz  
  
ADD ./configs /build-configs  
  
#  
# Install Java Server Tag Library  
#  
RUN wget
https://build.shibboleth.net/nexus/service/local/repositories/thirdparty/content/javax/servlet/jstl/1.2/jstl-1.2.jar
\  
-P /usr/share/tomcat/lib/  
  
#  
# Deploy to Tomcat  
#  
RUN mkdir -p /usr/local/tomcat/conf/Catalina/localhost/  
  
RUN mkdir -p /etc/shibboleth-idp/authn  
COPY relying-party.xml /etc/shibboleth-idp/relying-party.xml  
COPY password-authn-config.xml /etc/shibboleth-idp/authn/password-authn-
config.xml  
COPY kerberos/krb5.conf /etc/krb5.conf  
  
COPY install-shib.sh /install-shib.sh  
COPY start.sh /start.sh  
RUN chmod a+x /install-shib.sh  
RUN chmod a+x /start.sh  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
ENV DIST=/usr/local/dist/shibboleth-identity-provider-${version}  
ENV IDP_HOME=/opt/shibboleth-idp  
  
#RUN SCOPE=docker HOST=tier-idp.$SCOPE
ENTITYID=http://$HOST:8080/idp/shibboleth /install-shib.sh  
EXPOSE 8080  
CMD ["/start.sh"]  

