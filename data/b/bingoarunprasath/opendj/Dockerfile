FROM ubuntu:14.04  
MAINTAINER Arun prasath <arunprasath33@gmail.com>  
RUN apt-get -y update && apt-get install -y \  
openjdk-7-jre-headless \  
wget \  
unzip  
  
WORKDIR /opt  
RUN wget
http://download.forgerock.org/downloads/opendj/nightly/20151202_0028/OpenDJ-3.0.0-20151202.zip  
RUN unzip OpenDJ-3.0.0-20151202.zip  
  
ENV LDAP_PORT 1389  
ENV LDAPS_PORT 1636  
ENV ADMIN_CONN_PORT 4444  
ENV ROOT_USER_DN cn=Directory\ Manager  
ENV ROOT_USER_PASSWORD password  
# I shouldn't be doing this; links; coreos blah blah  
ENV OPENDJ_DIR /opt/opendj  
ENV BASE_DN "dc=example,dc=com"  
WORKDIR $OPENDJ_DIR  
RUN ./setup --cli -v \  
\--ldapPort $LDAP_PORT \  
\--ldapsPort $LDAPS_PORT \  
\--adminConnectorPort $ADMIN_CONN_PORT \  
\--rootUserDN "$ROOT_USER_DN" \  
\--baseDN $BASE_DN \  
\--rootUserPassword $ROOT_USER_PASSWORD \  
\--generateSelfSignedCertificate \  
\--no-prompt \  
\--noPropertiesFile \  
\--addBaseEntry \  
\--doNotStart  
  
COPY RunOpenDJ /opt/RunOpenDJ  
RUN chmod +x /opt/RunOpenDJ  
ENV PATH $OPENDJ_DIR/bin:$PATH  
#WORKDIR /install/opendj/bin  
ENTRYPOINT ["/opt/RunOpenDJ"]  
  
EXPOSE 1389 1636 4444  

