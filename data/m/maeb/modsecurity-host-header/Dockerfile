FROM fooinha/nginx-modsecurity  
  
RUN sed -i 's/^SecAuditLogParts .*/SecAuditLogParts BK/g'
/opt/spider/conf/modsecurity.conf &&\  
sed -i 's|^SecAuditLog .*|SecAuditLog /proc/self/fd/1|g'
/opt/spider/conf/modsecurity.conf &&\  
sed -i 's/^SecAuditEngine .*/SecAuditEngine On/g'
/opt/spider/conf/modsecurity.conf &&\  
sed -i 's/^SecRuleEngine .*/SecRuleEngine On/g'
/opt/spider/conf/modsecurity.conf &&\  
sed -i '/^Include .*/d' /opt/spider/conf/modsecurity.conf &&\  
echo "Include /opt/spider/conf/rules/modsecurity-host.conf" >>
/opt/spider/conf/modsecurity.conf  
  
RUN rm -rf /opt/spider/conf/rules/*  
COPY modsecurity-host.conf /opt/spider/conf/rules/  

