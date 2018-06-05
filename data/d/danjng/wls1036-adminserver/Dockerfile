# Version: 0.0.1 Weblogic 10.3.6 Basic Domain and Admin Server -- snagged from
unbc  
# Username: weblogic  
# Password: weblogic1 but set a runtime  
# http://<IP>:7001/console/  
# docker run -d -p <IP>:7001:7001 danjng/wls1036-adminserver <newpassword>  
# docker run -it -p 7001:7001 <Container ID> <password>  
FROM danjng/wls1036  
MAINTAINER Daniel Ng "danjng@gmail.com"  
USER root  
ADD basicWLSDomain_AdminServer.py
/u02/app/oracle/product/fmw/wlserver_10.3/common/templates/scripts/wlst/  
  
RUN /bin/bash -c "source
/u02/app/oracle/product/fmw/wlserver_10.3/server/bin/setWLSEnv.sh" \  
&& /u02/app/oracle/product/fmw/wlserver_10.3/common/bin/wlst.sh
/u02/app/oracle/product/fmw/wlserver_10.3/common/templates/scripts/wlst/basicWLSDomain_AdminServer.py  
  
ADD change_weblogic_password.sh /u02/app/oracle/product/fmw/  
  
ADD entrypoint.sh /u02/app/oracle/product/fmw/  
  
RUN [ "chmod", "a+x",
"/u02/app/oracle/product/fmw/change_weblogic_password.sh",
"/u02/app/oracle/product/fmw/entrypoint.sh" ]  
  
ENTRYPOINT [ "/u02/app/oracle/product/fmw/entrypoint.sh", "AdminServer" ]  
  
EXPOSE 7001

