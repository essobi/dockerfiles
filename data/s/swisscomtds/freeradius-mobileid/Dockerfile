FROM alpine:latest  
MAINTAINER Eva Ramon <eva.ramon@swisscom.com>  
  
# Environment settings and defaults if not passed  
ENV AP_ID="mid://dev.swisscom.ch"  
ENV AP_PREFIX="Test"  
ENV DEFAULT_LANGUAGE=en  
ENV UNIQUEID_CHECK=ifset  
ENV ALLOWED_MCC=  
ENV CLIENT_PWD=  
ENV LDAP_SERVER="ldap://yourserver.com"  
ENV LDAP_USERID="SystemLDAP,CN=Users,DC=org,DC=acme,DC=com"  
ENV LDAP_PWD="ThisMustStaySecret"  
ENV LDAP_BASEDN="CN=Users,DC=org,DC=acme,DC=ch"  
ENV LDAP_UPDATE=  
ENV LDAP_ATTR_MOBILE=mobile  
ENV LDAP_ATTR_LANGUAGE=preferredLanguage  
ENV LDAP_ATTR_SNOFDN=msNPCallingStationID  
  
# Install FreeRADIUS  
RUN apk update && apk upgrade \  
&& apk add --update curl openssl ca-certificates freeradius freeradius-ldap
freeradius-radclient bash git openldap-clients libxml2-utils tzdata \  
&& rm -rf /var/cache/apk/*  
  
# Set timezone  
ENV TZ=Europe/Brussels  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Install Mobile ID module  
WORKDIR /opt  
RUN git clone https://github.com/SCS-CBU-CED-IAM/freeradius-mobileid.git
freeradius \  
&& chown radius:radius -R /opt/freeradius/  
  
# Add files  
ADD install.sh /opt/install.sh  
RUN chmod +x /opt/install.sh  
  
# Expose ports  
EXPOSE 1812/udp  
EXPOSE 1813/udp  
  
# Run  
CMD /opt/install.sh;/usr/sbin/radiusd -f -x -l stdout  

