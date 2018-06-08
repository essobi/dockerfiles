FROM hachque/opensuse  
MAINTAINER James Rhodes  
  
# Configure zypper  
RUN zypper mr -e openSUSE_13.1_OSS  
RUN zypper mr -e openSUSE_13.1_Updates  
RUN zypper ref  
RUN bash -c 'zypper --non-interactive patch || true'  
RUN bash -c 'zypper --non-interactive patch || true'  
  
# Remove systemd targets  
RUN rm -R /usr/lib/systemd/system/* 2>/dev/null  
RUN rm -R /usr/lib/systemd/system-generators/* 2>/dev/null  
RUN rm -R /etc/systemd/system/* 2>/dev/null  
RUN rm -R /etc/init.d/* 2>/dev/null  
  
# Add the boot scripts  
ADD 00-patch /etc/init.simple/00-patch  
ADD 01-ssh /etc/init.simple/01-ssh  
  
# Allow logins without audit kernel module.  
RUN sed -r -n -i '/session(\s+)required(\s+)pam_loginuid/{s|^|#|};p'
/etc/pam.d/login  
RUN sed -r -n -i '/session(\s+)required(\s+)pam_loginuid/{s|^|#|};p'
/etc/pam.d/sshd  
  
# Expose SSH.  
EXPOSE 22  
# Add the init script  
ADD init /init  
  
# Set /init as the default  
CMD ["/init"]  

