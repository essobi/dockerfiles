# I know I should attach to a particular revision... but  
# let's just ride on *latest* for the time being.  
FROM phusion/baseimage:latest  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Enable ssh service and expose port 22  
RUN rm -f /etc/service/sshd/down  
EXPOSE 22  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
# RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
# Volume holding the user's CA certificate  
# VOLUME /etc/ssh/users_ca.pub  
# Add the proper configuration to SSH config file  
RUN echo "TrustedUserCAKeys /etc/ssh/users_ca.pub" >> /etc/ssh/sshd_config; \  
echo "PasswordAuthentication no" >> /etc/ssh/sshd_config  
  
# Run the user management script at boot time  
ADD users /etc/my_init.d/users  

