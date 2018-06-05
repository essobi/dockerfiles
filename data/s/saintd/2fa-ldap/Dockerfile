FROM debian:latest  
  
RUN apt-get update && apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
libnss-ldap libpam-ldap nscd libpam-google-authenticator openssh-server  
  
RUN /bin/echo "session required pam_mkhomedir.so" >> /etc/pam.d/common-session  
  
# Dont need to run google-authenticator if you have the config file already  
ADD .google_authenticator /etc/ssh/.google_authenticator  
RUN chmod 0400 /etc/ssh/.google_authenticator  
  
ADD id_rsa.pub /root/.ssh/authorized_keys  
  
RUN /bin/sed -i 's/^session.*required.*pam_loginuid.so$/session optional
pam_loginuid.so/g; 3i # Google Authentication\nauth sufficient
pam_google_authenticator.so user=root
secret=\/etc\/ssh\/.google_authenticator\n' /etc/pam.d/sshd  
  
RUN /bin/sed -i 's/compat/compat ldap/g' /etc/nsswitch.conf  
  
# Config LDAP  
# NOTE: If root auth is required, "PermitRootLogin yes" must be set instead of
"without-password".  
RUN /bin/sed -i 's/^ChallengeResponseAuthentication
no$/ChallengeResponseAuthentication yes/g;s/^PermitRootLogin.*/PermitRootLogin
yes\nAuthenticationMethods publickey,keyboard-interactive/g'
/etc/ssh/sshd_config && mkdir /var/run/sshd  
  
EXPOSE 22  
COPY ldap-config.sh /ldap-config.sh  
CMD /ldap-config.sh && /usr/sbin/sshd -D  
  
# BUILD: docker build -t 2fa .  
# RUN: docker run -d -p 22 -e LDAP_BASE="dc=ldap,dc=example,dc=org" -e
LDAP_HOSTNAME="172.17.1.109" -e
LDAP_BINDDN="cn=admin,dc=ldap,dc=example,dc=org" -e
LDAP_BINDPW="mysecretpassword" 2fa  
# To setup the mobile App: Install it, Set up account -> Enter provided key ->
Type the first line from the .google_authenticator file.  
# Then ssh the container as root with your private key and provide the Google
Authenticator code:  
# Quick test in local: ssh -p <docker-port> root@localhost  

