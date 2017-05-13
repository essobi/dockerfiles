FROM learninglayers/base

MAINTAINER Petru Nicolaescu

# Add MITREid config files
ADD etc /etc/

CMD sed -i "s#OIDC_DB_USER#${OIDC_DB_USER}#g" /etc/mitreid-connect/data-context.xml && \
	sed -i "s#OIDC_DB_PASS#${OIDC_DB_PASS}#g" /etc/mitreid-connect/data-context.xml && \
	sed -i "s#LAYERS_API_URI#${LAYERS_API_URI}#g" /etc/mitreid-connect/server-config.xml && \
	sed -i "s#LDAP_ROOT_DN#${LDAP_ROOT_DN}#g" /etc/mitreid-connect/user-context.xml && \
	sed -i "s#LDAP_ADMINS#${LDAP_ADMINS}#g" /etc/mitreid-connect/user-context.xml
	
VOLUME ["/etc/mitreid-connect/","/etc/sql/"]
