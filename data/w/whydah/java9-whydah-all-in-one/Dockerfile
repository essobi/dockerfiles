# This is a comment  
FROM cantara/alpine-zulu-jdk9  
MAINTAINER Totto <totto@totto.org>  
RUN apk update  
#RUN yum install -y yum-cron  
RUN apk-install wget apache2  
  
# Install sshd - should probably be fortified  
RUN apk-install openssh  
RUN mkdir /var/run/sshd  
RUN echo 'root:kjempehemmelig4' | chpasswd  
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN echo "export VISIBLE=now" >> /etc/profile  
#RUN /usr/sbin/sshd-keygen  
RUN adduser -D -s /bin/sh SSOLoginWebApp  
RUN adduser -D -s /bin/sh SecurityTokenService  
RUN adduser -D -s /bin/sh TestWebApp  
RUN adduser -D -s /bin/sh UserAdminService  
RUN adduser -D -s /bin/sh UserAdminWebApp  
RUN adduser -D -s /bin/sh UserIdentityBackend  
  
## Install SSOLoginWebApp  
# ADD https://raw.githubusercontent.com/cantara/Whydah-
SSOLoginWebApp/master/update-service.sh /home/SSOLoginWebApp/update_service.sh  
# RUN chmod 755 /home/SSOLoginWebApp/update_service.sh  
# RUN chown SSOLoginWebApp /home/SSOLoginWebApp/update_service.sh  
## Install SSOLoginWebApp  
RUN su - SSOLoginWebApp -c "wget -O update-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-SSOLoginWebApp/master/update-
service.sh"  
RUN su - SSOLoginWebApp -c "/usr/bin/wget -O start-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-SSOLoginWebApp/master/start-
service.sh"  
RUN chmod 755 /home/SSOLoginWebApp/*.sh  
RUN su - SSOLoginWebApp -c "/usr/bin/wget -O ssologinservice.PROD.properties
-q -N https://raw.githubusercontent.com/cantara/Whydah-
SSOLoginWebApp/master/src/main/resources/ssologinwebapp.TEST_LOCALHOST.properties"  
RUN su - SSOLoginWebApp -c "/home/SSOLoginWebApp/update-service.sh"  
#RUN su - SSOLoginWebApp -c "/home/SSOLoginWebApp/start-service.sh &"  
## Install SecurityTokenService  
RUN su - SecurityTokenService -c "/usr/bin/wget -O update-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-
SecurityTokenService/master/update-service.sh"  
RUN su - SecurityTokenService -c "/usr/bin/wget -O start-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-
SecurityTokenService/master/start-service.sh"  
RUN chmod 755 /home/SecurityTokenService/*.sh  
RUN su - SecurityTokenService -c "/usr/bin/wget -O
securitytokenservice.PROD.properties -q -N
https://raw.githubusercontent.com/cantara/Whydah-
SecurityTokenService/master/src/main/resources/securitytokenservice.TEST_LOCALHOST.properties"  
RUN su - SecurityTokenService -c "/home/SecurityTokenService/update-
service.sh"  
#RUN su - SecurityTokenService -c "/home/SecurityTokenService/start-service.sh
&"  
## Install TestWebApp  
RUN su - TestWebApp -c "/usr/bin/wget -O update-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-TestWebApp/master/update-
service.sh"  
RUN su - TestWebApp -c "/usr/bin/wget -O start-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-TestWebApp/master/start-
service.sh"  
RUN chmod 755 /home/TestWebApp/*.sh  
RUN su - TestWebApp -c "/usr/bin/wget -O testwebapp.TEST.properties -q -N
https://raw.githubusercontent.com/cantara/Whydah-
TestWebApp/master/testwebapp.TEST.properties"  
RUN su - TestWebApp -c "/home/TestWebApp/update-service.sh"  
#RUN su - TestWebApp -c "/home/TestWebApp/start-service.sh &"  
## Install UserAdminService  
RUN su - UserAdminService -c "/usr/bin/wget -O update-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-
UserAdminService/master/update-service.sh"  
RUN su - UserAdminService -c "/usr/bin/wget -O start-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-
UserAdminService/master/start-service.sh"  
RUN chmod 755 /home/UserAdminService/*.sh  
RUN su - UserAdminService -c "/usr/bin/wget -O
useradminservice_override.properties -q -N
https://raw.githubusercontent.com/Cantara/Whydah-
UserAdminService/master/useradminservice_override.properties.example"  
RUN su - UserAdminService -c "/home/UserAdminService/update-service.sh"  
#RUN su - UserAdminService -c "/home/UserAdminService/start-service.sh &"  
## Install UserAdminWebApp  
RUN su - UserAdminWebApp -c "/usr/bin/wget -O update-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-
UserAdminWebApp/master/update-service.sh"  
RUN su - UserAdminWebApp -c "/usr/bin/wget -O start-service.sh -q -N
https://raw.githubusercontent.com/cantara/Whydah-UserAdminWebApp/master/start-
service.sh"  
RUN chmod 755 /home/UserAdminWebApp/*.sh  
RUN su - UserAdminWebApp -c "/usr/bin/wget -O useradminwebapp.PROD.properties
-q -N https://raw.githubusercontent.com/cantara/Whydah-
UserAdminWebApp/master/src/main/resources/useradminwebapp.TEST_LOCALHOST.properties"  
RUN su - UserAdminWebApp -c "/home/UserAdminWebApp/update-service.sh"  
#RUN su - UserAdminWebApp -c "/home/UserAdminWebApp/start-service.sh &"  
## Install UserIdentityBackend  
RUN su - UserIdentityBackend -c "/usr/bin/wget --no-cache -O update-service.sh
-q -N
https://raw.githubusercontent.com/Cantara/Whydah/master/config/Docker/uib/uib-
all-in-one/toRoot/update-service.sh"  
RUN su - UserIdentityBackend -c "/usr/bin/wget -O start-service.sh -q -N
https://raw.githubusercontent.com/Cantara/Whydah/master/config/Docker/uib/uib-
all-in-one/toRoot/start-service.sh"  
RUN chmod 755 /home/UserIdentityBackend/*.sh  
RUN su - UserIdentityBackend -c "/home/UserIdentityBackend/update-service.sh"  
RUN su - UserIdentityBackend -c "mkdir
/home/UserIdentityBackend/bootstrapdata"  
RUN su - UserIdentityBackend -c "mkdir
/home/UserIdentityBackend/bootstrapdata/ldap"  
RUN su - UserIdentityBackend -c "mkdir
/home/UserIdentityBackend/bootstrapdata/hsqldb"  
RUN su - UserIdentityBackend -c "mkdir
/home/UserIdentityBackend/bootstrapdata/lucene"  
RUN su - UserIdentityBackend -c "mkdir /home/UserIdentityBackend/testdata"  
COPY testdata /home/UserIdentityBackend/testdata  
RUN su - UserIdentityBackend -c "/usr/bin/wget -O
useridentity.override.properties -q -N
https://raw.githubusercontent.com/Cantara/Whydah-
UserIdentityBackend/master/useridentitybackend.override.properties"  
COPY testdata /home/UserIdentityBackend/prodInitData  
  
RUN su - UserIdentityBackend -c "/home/UserIdentityBackend/start-service.sh &"  
  
## New Constretto start  
ADD start-service-uib-dev-contretto.sh /home/UserIdentityBackend/start-
service.sh  
RUN chmod 755 /home/UserIdentityBackend/*.sh  
  
## Install Apache and set up proxypasses  
# RUN yum install -y httpd  
RUN /usr/bin/wget -O /etc/apache2/conf.d/whydah.conf -q -N
https://raw.githubusercontent.com/cantara/Whydah/master/config/apache/whydah.conf  
  
## Set up start of services  
RUN apk-install py-setuptools  
RUN apk-install supervisor  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
#RUN ln -s /etc/supervisor/conf.d/supervisord.conf /usr/etc/supervisord.conf  
## Simple start-all for working inside the image  
RUN echo "#!/bin/sh" > /root/start_whydah.sh  
RUN echo "/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf &"
>>/root/start_whydah.sh  
RUN chmod 755 /root/start_whydah.sh  
RUN ln -s /usr/local/java/bin/java /usr/bin/java  
  
EXPOSE 22 80 9990 9992 9995 9996 9997 9998  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

