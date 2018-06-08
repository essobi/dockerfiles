#  
# Dockerfile for Payara 4.1.1.154 NO Hazelcast  
#  
# realsoft/payara:4.1.1.154  
FROM realsoft/java:8  
MAINTAINER Emil Hurmuzov <emil@hurmuzov.com>  
  
ENV PAYARA_PKG https://s3-eu-
west-1.amazonaws.com/payara.co/Payara+Downloads/Payara+4.1.1.154/payara-4.1.1.154.zip  
ENV PKG_FILE_NAME payara-4.1.1.154.zip  
  
  
# add payara user, download payara build and unzip  
RUN \  
useradd -b /opt -m -s /bin/bash payara && echo payara:payara | chpasswd && \  
cd /opt && curl -O $PAYARA_PKG && unzip $PKG_FILE_NAME && rm $PKG_FILE_NAME &&
\  
chown -R payara:payara /opt/payara41* && \  
apt-get clean  
  
# default glassfish ports  
EXPOSE 4848 8080 8181 8686  
# Set up payara user and the home directory for the user  
USER payara  
WORKDIR /opt/payara41/glassfish/bin  
  
# User: admin / Pass: glassfish  
RUN echo
"admin;{SSHA256}80e0NeB6XBWXsIPa7pT54D9JZ5DR5hGQV1kN1OAsgJePNXY6Pl0EIw==;asadmin"
> /opt/payara41/glassfish/domains/payaradomain/config/admin-keyfile && \  
echo "AS_ADMIN_PASSWORD=glassfish" > pwdfile  
  
# enable secure admin to access DAS remotely. Note we are using the domain
payaradomain. Plus JMX  
RUN \  
./asadmin start-domain payaradomain && \  
./asadmin --user admin --passwordfile pwdfile enable-secure-admin && \  
./asadmin --user admin --passwordfile pwdfile create-jvm-options
-Dcom.sun.management.jmxremote:-Dcom.sun.management.jmxremote.port=8686:-Dcom.sun.management.jmxremote.local.only=false:-Dcom.sun.management.jmxremote.authenticate=false:-Dcom.sun.management.jmxremote.ssl=false
&& \  
./asadmin stop-domain payaradomain  
  
RUN echo "export PATH=$PATH:/opt/payara41/glassfish/bin" >>
/opt/payara/.bashrc  
  
# default command to run on container boot  
# CMD ["/opt/payara41/glassfish/bin/asadmin", "start-domain", "-v=true",
"payaradomain"]  

