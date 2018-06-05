# Docker registry repo/image used as our base  
FROM ctarwater/kali-msf-micro  
  
# Who is responsible for this madness?  
MAINTAINER ctarwater@blackfinsecurity.com  
  
# Let our non-root user start the services needed to run the Metasploit
Framework Console  
RUN echo "thastudent ALL = NOPASSWD: /usr/sbin/service postgresql *" >>
/etc/sudoers  
RUN echo "thastudent ALL = NOPASSWD: /usr/sbin/service metasploit *" >>
/etc/sudoers  
RUN echo "thastudent ALL = NOPASSWD: /usr/bin/msfconsole *" >> /etc/sudoers  
  
# Add our script to start the metasploit console  
RUN rm /init.sh  
ADD ./init.sh /init.sh  
  
# Create a non-root user  
RUN useradd -m thastudent && \  
chown -R thastudent:thastudent /home/thastudent  
  
# Issue remaining commands as new user  
USER thastudent  
  
# Issue commands from this directory  
WORKDIR /home/thastudent  
  
# We need to run multiple commands to get the msf running, so we put them into
a single script  
CMD ["/init.sh"]

