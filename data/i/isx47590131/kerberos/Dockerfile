# @edt ASIX-m11 Curs 2017-2018  
# kerberos host  
#servidor ssh amb kerberos creacio interactiu  
#-----------------------------------------------------------------------  
FROM fedora:24  
MAINTAINER asixm11@edt "@edt ASIX-m11"  
RUN dnf -y install nmap procps krb5-libs krb5-workstation openssh openssh-
clients passwd \  
pam_krb5 finger util-linux-user  
RUN mkdir /opt/docker/  
COPY * /opt/docker/  
RUN chmod +x /opt/docker/create_users.sh  
RUN rm -rf /var/run/nologin  
RUN cp /opt/docker/krb5.conf /etc/  
RUN cp -r /etc/pam.d /etc/oldpam.d  
RUN cp /opt/docker/chfn /etc/pam.d/  
RUN cp /opt/docker/login /etc/pam.d/  
RUN cp /opt/docker/system-auth /etc/pam.d/  
RUN sh /opt/docker/create_users.sh  
WORKDIR /opt/docker/  
CMD ["/bin/bash"]  

