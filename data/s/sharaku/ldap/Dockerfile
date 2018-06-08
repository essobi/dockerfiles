FROM debian:7.8  
MAINTAINER sharaku  
  
  
# ######################################################################  
# Install openldap, phpldapadmin, nginx, sshd  
  
# update  
RUN apt-get -y update  
  
# Install nginx.  
RUN apt-get install -y nginx php5-fpm  
  
# Install openldap (slapd) and ldap-utils  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-
recommends slapd ldap-utils openssl  
  
# Install phpldapadmin.  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-
recommends phpldapadmin  
  
# install sshd  
RUN \  
apt-get install -y openssh-server && \  
mkdir /var/run/sshd && \  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
# install git  
RUN apt-get install -y git  
  
# install cli  
RUN git clone https://github.com/sharaku/cli.git /opt/cli  
  
# ######################################################################  
# add settings  
  
RUN mkdir /opt/slapd  
ADD service/slapd/slapd.sh /opt/slapd/slapd.sh  
ADD service/slapd/setup.sh /opt/slapd/setup.sh  
  
RUN mkdir /opt/phpldapadmin  
ADD service/phpldapadmin/ldapadmin.sh /opt/phpldapadmin/ldapadmin.sh  
  
RUN mkdir /opt/sshd  
ADD service/sshd/start.sh /opt/sshd/start.sh  
ADD cli /opt/cli/command  
  
# start shell  
ADD start.sh /opt/start.sh  
  
# permission setting  
RUN \  
chmod -R 555 \  
/opt/start.sh \  
/opt/slapd/slapd.sh /opt/slapd/setup.sh\  
/opt/phpldapadmin/ldapadmin.sh \  
/opt/sshd/start.sh /opt/cli  
  
# phpLDAPadmin nginx config  
ADD service/nginx/phpldapadmin.nginx /etc/nginx/sites-available/phpldapadmin  
  
# CLI(ssh) config  
  
# ######################################################################  
# Default configuration: can be overridden at the docker command line  
ENV LDAP_DOMAIN example.com  
ENV LDAP_ADMIN_PWD toor  
ENV LDAP_ORGANISATION docker.io Example Inc.  
  
# ######################################################################  
# Clear out the local repository of retrieved package files  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose port 80, 389 must  
EXPOSE 22  
EXPOSE 80  
EXPOSE 389  
  
# To store the data outside the container, mount /var/lib/ldap as a data
volume  
VOLUME /var/lib/ldap  
VOLUME /etc/ldap/slapd.d  
  
# start  
CMD ["/opt/start.sh"]  
# ######################################################################  
# docker run -d \  
# -v /path/to/ldap/data/:/var/lib/ldap:rw \  
# -v /path/to/ldap/etc/ldap/slapd.d/:/etc/ldap/slapd.d:rw \  
# -e LDAP_DOMAIN=example.com \  
# -e LDAP_ADMIN_PWD=toor \  
# -e LDAP_ORGANISATION=docker.io Example Inc. \  
# -p 389:389 \  
# -p 80:80 \  
# sharaku/ldap  
#

