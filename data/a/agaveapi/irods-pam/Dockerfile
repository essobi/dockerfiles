######################################################  
#  
# Agave IRODS + PAM Server  
# Tag: agaveapi/irods-pam  
#  
# This is the iRODS server configured with PAM support  
# used for testing iRODS PAM support in the Agave API.  
# It extends from the agaveapi/centos-base and maps  
# the existing testuser, testotheruser, and testshareuser  
# to accounts in irods.  
#  
# Usage:  
# docker run -h docker.example.com -i \  
# -p 1247:1247 \ # IRODS + PAM  
# -p 10022:22 \ # SSHD, SFTP  
# agaveapi/irods-pam  
#  
# https://bitbucket.org/taccaci/agave-environment  
#  
######################################################  
FROM agaveapi/irods  
  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>  
  
USER root  
RUN yum -y install --enablerepo=centosplus openssl-devel pam-devel  
  
# Update default makefile configs to build PAM support into the server  
RUN sed -ri 's/# PAM_AUTH = 1/PAM_AUTH = 1/g'
/home/irods/iRODS/config/config.mk  
RUN sed -ri 's/# USE_SSL = 1/USE_SSL = 1/g' /home/irods/iRODS/config/config.mk  
  
# Build whole shebang from scratch using added config files.  
WORKDIR /home/irods/iRODS  
ADD irods/irods.pam /etc/pam.d/irods  
RUN su - irods -c "cd /home/irods/iRODS && scripts/configure"  
RUN su - irods -c "cd /home/irods/iRODS && make"  
  
# Update PAM script permissions  
RUN chown root server/bin/PamAuthCheck  
RUN chmod u+s server/bin/PamAuthCheck  
  
# create SSL certs for communication with clients  
USER irods  
RUN mkdir /home/irods/iRODS/config/ssl  
WORKDIR /home/irods/iRODS/config/ssl  
RUN openssl genrsa -out server.key 1024  
RUN openssl req -subject -new -subj "/C=US/O=Texas Advanced Computing
Center/OU=Dev Certificate Authorities/OU=dockerCA/CN=docker.example.com" -x509
-key server.key -out server.crt -days 3650  
RUN openssl dhparam -2 -out dhparams.pem 2048  
RUN printf '\nexport
irodsSSLCertificateChainFile=/home/irods/iRODS/config/ssl/server.crt' >>
/home/irods/.bashrc  
RUN printf '\nexport
irodsSSLCertificateKeyFile=/home/irods/iRODS/config/ssl/server.key' >>
/home/irods/.bashrc  
RUN printf '\nexport
irodsSSLDHParamsFile=/home/irods/iRODS/config/ssl/dhparams.pem' >>
/home/irods/.bashrc  
  
# Finish iRODS setup  
USER root  
WORKDIR /home/irods/iRODS  
RUN su - irods -c "cd /home/irods/iRODS && scripts/finishSetup --noask
--verbose"  
  
# Add users and run jargon specquery commands so permissions work in jargon  
ADD irods/user_setup.sh /home/irods/iRODS/scripts/user_setup.sh  
RUN chown irods:irods /home/irods/iRODS/scripts/user_setup.sh  
RUN chmod 755 /home/irods/iRODS/scripts/user_setup.sh  
  
# Add system users to mirror accounts since we're not using a pam config on
this one  
RUN su - irods -c "/home/irods/iRODS/irodsctl start && \  
. /home/irods/iRODS/scripts/user_setup.sh && \  
/home/irods/iRODS/irodsctl stop"  
  
# Set up user environment accounting for docker hostname at build time  
#ADD irods/irodsEnv /home/irods/.irods/.irodsEnv  
#RUN chown -R irods:irods /home/irods/.irods/.irodsEnv  
# Add supervisor to startup sshd, postgres, and irods  
ADD supervisord.conf /etc/supervisord.conf  
  
#VOLUME ["/data"]  
EXPOSE 10389 22 5432 1247  
CMD ["/usr/bin/supervisord"]  

