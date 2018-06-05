######################################################  
#  
# Agave DevOps MyProxy Server  
# Tag: agaveapi/myproxy  
#  
# This container provides a standard myproxy server running  
# on port 7512 for the test users created in the agaveapi/centos-base  
# image. It also provides a myproxy server configured with a  
# trust relationship runing on port 7513. The trusted grid  
# cert and key will be printed when the container starts.  
#  
# Usage:  
# docker run -h docker.example.com -i \  
# -p 7512:7512 \ # MyProxy CA + PAM  
# -p 7513:7513 \ # MyProxy CA with trust relationship  
# -p 10022:22 \ # SSHD, SFTP  
# agaveapi/myproxy  
#  
# https://bitbucket.org/taccaci/agave-environment  
#  
######################################################  
FROM agaveapi/centos-base  
  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>  
  
RUN yum -y localinstall http://repo.grid.iu.edu/osg-el6-release-latest.rpm  
RUN yum -y localinstall http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install myproxy  
RUN yum -y install myproxy myproxy-server myproxy-admin myproxy-doc globus-
simple-ca perl-Text-CSV perl-Email-Valid bind-utils libtool gcc-c++ igtf-ca-
certs  
  
# Setup simple ca  
RUN grid-ca-create -subject "CN=Docker MyProxy, OU=dockerCA, OU=Dev
Certificate Authorities, O=Texas Advanced Computing Center, C=US" \  
-email root@docker.example.com \  
-pass globus \  
-days 3650  
  
# Create symlinks for grid ca tools to work  
RUN ln -s /var/lib/globus/simple_ca/globus-host-ssl.conf /etc/grid-security/
&& \  
ln -s /var/lib/globus/simple_ca/globus-user-ssl.conf /etc/grid-security/ && \  
ln -s /var/lib/globus/simple_ca/grid-security.conf /etc/grid-security/  
  
# double default cert length  
RUN sed -ri 's/default_bits = 1024/default_bits = 2048/g'
/var/lib/globus/simple_ca/globus-host-ssl.conf  
  
# generate and sign a hostcert  
RUN cd /etc/grid-security ; grid-cert-request -host docker.example.com  
RUN cd /etc/grid-security; echo "globus" | grid-ca-sign -days 3650 -in
hostcert_request.pem -out hostcert.pem  
  
# copy cert and key to proper locations  
RUN cp /var/lib/globus/simple_ca/newcerts/01.pem /etc/grid-
security/myproxy/hostcert.pem  
RUN cp /etc/grid-security/hostkey.pem /etc/grid-security/myproxy/hostkey.pem  
  
RUN chown -R root:root /var/lib/myproxy  
RUN chown -R myproxy:myproxy /var/lib/globus/simple_ca  
RUN CERT_HASH=$(openssl x509 -in /var/lib/globus/simple_ca/cacert.pem -noout
-hash) && \  
ln -s /var/lib/globus/simple_ca/cacert.pem $CERT_HASH.0  
  
# Add myproxy config files  
ADD myproxy/myproxy-server.config /etc/myproxy-server.config  
ADD myproxy/myproxy-server-trusted.config /etc/myproxy-server-trusted.config  
ADD myproxy/myproxy.pam /etc/pam.d/myproxy  
  
# Env variables needed by myproxy-server  
ENV X509_USER_CERT /etc/grid-security/myproxy/hostcert.pem  
ENV X509_USER_KEY /etc/grid-security/myproxy/hostkey.pem  
  
RUN echo '"/C=US/O=Texas Advanced Computing Center/OU=Dev Certificate
Authorities/OU=dockerCA/CN=testuser" testuser' >> /etc/grid-security/grid-
mapfile  
RUN echo '"/C=US/O=Texas Advanced Computing Center/OU=Dev Certificate
Authorities/OU=dockerCA/CN=testshareuser" testshareuser' >> /etc/grid-
security/grid-mapfile  
RUN echo '"/C=US/O=Texas Advanced Computing Center/OU=Dev Certificate
Authorities/OU=dockerCA/CN=testother" testother' >> /etc/grid-security/grid-
mapfile  
RUN chmod +r /etc/grid-security/grid-mapfile  
  
# generate and sign a service cert  
WORKDIR /myproxy-gateway  
RUN mkdir hostcerts;  
WORKDIR /myproxy-gateway/hostcerts  
RUN grid-cert-request -host docker.example.com -dir . -service mpg -prefix mpg
-nopw  
RUN echo "globus" | grid-ca-sign -days 3650 -in mpgcert_request.pem -out
mpgcert.pem  
RUN openssl rsa -in mpgkey.pem -outform PEM -out new-mpgkey.pem  
  
ADD supervisord.conf /etc/supervisord.conf  
RUN mkdir /var/log/supervisor  
RUN chmod -R 777 /var/log/supervisor  
ADD docker_entrypoint.sh /docker_entrypoint.sh  
ADD create_hostcert /usr/local/bin/create_hostcert  
  
ENV MYPROXY_SERVER_DN "/C=US/O=Texas Advanced Computing Center/OU=Dev
Certificate Authorities/OU=dockerCA/CN=host/docker.example.com"  
ENTRYPOINT [ "/docker_entrypoint.sh" ]  
EXPOSE 10389 22 7512 7513  
CMD [ "/usr/bin/supervisord" ]  

