FROM gui81/alfresco:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-
mappings="21:21/tcp,137:137/tcp,138:138/tcp,139:139/tcp,445:445/tcp,7070:7070/tcp,8009:8009/tcp,8080:8080/tcp,8443:8443/tcp"
\  
org.freenas.privileged="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=8080 \  
org.freenas.web-ui-path="share" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/content\", \  
\"descr\": \"Alfresco content directory\" \  
}, \  
{ \  
\"name\": \"/alfresco/alf_data\", \  
\"descr\": \"Alfresco Data Folder\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"ALFRESCO_HOSTNAME\", \  
\"descr\": \"hostname of the Alfresco server; default = localhost\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ALFRESCO_PORT\", \  
\"descr\": \"port for afresco to listen to; default = 8080 if protocol is http
or 8443 if protocol is https\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ALFRESCO_PROTOCOL\", \  
\"descr\": \"protocol used by alfresco to generate links; default = http\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"AMP_DIR_ALFRESCO\", \  
\"descr\": \"directory containing AMP files (modules) for alfresco.war (bind
mount as volume)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"AMP_DIR_SHARE\", \  
\"descr\": \"directory containing AMP files (modules) for share.war (bind
mount as volume)\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CIFS_ENABLED\", \  
\"descr\": \"whether or not to enable CIFS; default = true\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CIFS_SERVER_NAME\", \  
\"descr\": \"hostname of the CIFS server; default = localhost\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CIFS_DOMAIN\", \  
\"descr\": \"domain of the CIFS server; default = WORKGROUP\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CONTENT_STORE\", \  
\"descr\": \"where content is stored; default = /content\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_CONN_PARAMS\", \  
\"descr\": \"database connection parameters; for MySQL, default =
?useSSL=false, otherwise empty\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_HOST\", \  
\"descr\": \"host of the database server; default = localhost\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_KIND\", \  
\"descr\": \"postgresql or mysql; default = postgresql\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_NAME\", \  
\"descr\": \"name of the database to connect to; default = alfresco\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_PASSWORD\", \  
\"descr\": \"password to use when connecting to the database; default =
admin\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_USERNAME\", \  
\"descr\": \"username to use when connecting to the database; default =
alfresco\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DB_PORT\", \  
\"descr\": \"port of the database server; default = 5432\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"FTP_PORT\", \  
\"descr\": \"port of the ftp server; default = 5432\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LDAP_ENABLED\", \  
\"descr\": \"whether or not to enable LDAP; default = false\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LDAP_KIND\", \  
\"descr\": \"ldap (e.g. for OpenLDAP) or ldap-ad (Active Directory); default =
ldap\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LDAP_AUTH_USERNAMEFORMAT\", \  
\"descr\": \"default = uid=%s,cn=users,cn=accounts,dc=example,dc=com\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LDAP_URL\", \  
\"descr\": \"URL of LDAP server; default = ldap://ldap.example.com:389\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LDAP_DEFAULT_ADMINS\", \  
\"descr\": \"comma separated list of admin names in ldap; default = admin\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LDAP_SECURITY_PRINCIPAL\", \  
\"descr\": \"default = uid=admin,cn=users,cn=accounts,dc=example,dc=com\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LDAP_SECURITY_CREDENTIALS\", \  
\"descr\": \"default = password\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LDAP_GROUP_SEARCHBASE\", \  
\"descr\": \"default = cn=groups,cn=accounts,dc=example,dc=com\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_HOST\", \  
\"descr\": \"hostname or IP where email should be sent; default = localhost\",
\  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_PORT\", \  
\"descr\": \"default = 25\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_USERNAME\", \  
\"descr\": \"username to connect to the smtp server\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_PASSWORD\", \  
\"descr\": \"password to connect to the smtp server\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_FROM_DEFAULT\", \  
\"descr\": \"what is in the from field; default = alfresco@alfresco.org\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_PROTOCOL\", \  
\"descr\": \"smtp or smtps; default = smtp\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_SMTP_AUTH\", \  
\"descr\": \"is authentication required or not; default = false\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_SMTP_STARTTLS_ENABLE\", \  
\"descr\": \"use starttls or not; default = false\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_SMTPS_AUTH\", \  
\"descr\": \"is authentication required or not; default = false\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MAIL_SMTPS_STARTTLS_ENABLE\", \  
\"descr\": \"use starttls or not; default = false\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"NFS_ENABLED\", \  
\"descr\": \"whether or not to enable NFS; default = true\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"SHARE_HOSTNAME\", \  
\"descr\": \"hostname of the share server; default = localhost\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"SHARE_PORT\", \  
\"descr\": \"port for share to listen to; default = 8080 if protocol is http
or 8443 if protocol is https\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"SHARE_PROTOCOL\", \  
\"descr\": \"protocol use by share to generate links; default = http\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"SYSTEM_SERVERMODE\", \  
\"descr\": \"the server running mode for you system; default = PRODUCTION\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"TOMCAT_CSRF_ENABLED\", \  
\"descr\": \"Disable the tomcat CSRF policy; default = false\", \  
\"optional\": true \  
} \  
]"  

