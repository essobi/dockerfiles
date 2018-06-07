FROM learninglayers/base  
  
MAINTAINER Aarij Siddiqui  
  
ADD clvitra/ /etc/clvitra  
  
CMD sed -i "s#LAYERS_API_URI#${LAYERS_API_URI}#g" /etc/clvitra/base.properties
&& \  
  
sed -i "s#CLVITRA_DB_NAME#${CLVITRA_DB_NAME}#g"
/etc/clvitra/dbconnection.properties && \  
sed -i "s#CLVITRA_DB_USER#${CLVITRA_DB_USER}#g"
/etc/clvitra/dbconnection.properties && \  
sed -i "s#CLVITRA_DB_PASS#${CLVITRA_DB_PASS}#g"
/etc/clvitra/dbconnection.properties && \  
  
sed -i "s#LAYERS_API_URI#${LAYERS_API_URI}#g" /etc/clvitra/oidc.properties &&
\  
sed -i "s#CLVITRA_OIDC_CLIENT_ID#${CLVITRA_OIDC_CLIENT_ID}#g"
/etc/clvitra/oidc.properties && \  
sed -i "s#CLVITRA_OIDC_CLIENT_SECRET#${CLVITRA_OIDC_CLIENT_SECRET}#g"
/etc/clvitra/oidc.properties  
  
VOLUME ["/etc/clvitra","/etc/sql/"]

