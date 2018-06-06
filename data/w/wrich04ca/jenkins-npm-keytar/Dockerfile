# This Dockerfile is used to build an image capable of running the npm keytar
node module  
# IT MUST BE RUN AS PRIVELEGED IN ORDER TO PROPERLY OPERATE  
FROM wrich04ca/jenkins-npm-agent  
  
# Installs the libsecret library required by keytar  
RUN apt-get install -y gnome-keyring libsecret-1-dev  
  
# Copy the PAM configuration to allow unlocking of the gnome keyring  
RUN rm /etc/pam.d/login  
COPY login /etc/pam.d/login  
  
# Add to the .bashrc configuration with additional options for auto launching
a dbus-session  
COPY .bashrc /home/jenkins/.bashrc_temp  
RUN cat /home/jenkins/.bashrc_temp>>/home/jenkins/.bashrc  
RUN rm /home/jenkins/.bashrc_temp  
  
CMD ["/usr/sbin/sshd", "-D"]  

