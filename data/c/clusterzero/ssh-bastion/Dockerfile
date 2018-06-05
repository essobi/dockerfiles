FROM ubuntu:14.04  
MAINTAINER Sebastian Scatularo <sebastian@cluster-zero.com>  
  
RUN apt-get update && apt-get install -y gettext openssh-server libnss-ldap
libpam-ldap nscd  
RUN mkdir /var/run/sshd  
RUN mkdir /var/run/nscd  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
COPY etc/ldap.conf.tpl /etc/ldap.conf.tpl  
COPY etc/nsswitch.conf /etc/nsswitch.conf  
COPY etc/pam.d/common-session /etc/pam.d/common-session  
COPY etc/pam.d/sshd /etc/pam.d/sshd  
  
ENV LDAP_BASE dc=test,dc=com  
ENV LDAP_HOST localhost:389  
ENV LDAP_BIND_DN cn=admin,dc=test,dc=com  
ENV LDAP_BIND_PWD secret  
  
EXPOSE 22  
ADD entrypoint /bin/entrypoint  
RUN chmod +x /bin/entrypoint  
ENTRYPOINT ["/bin/entrypoint"]  
CMD ["/usr/sbin/sshd", "-D"]  

