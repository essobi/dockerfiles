FROM phusion/passenger-ruby22:0.9.15  
# Set correct environment variables.  
ENV HOME /root  
ENV PASSENGER_APP_ENV development  
  
# enable ssh  
RUN rm -f /etc/service/sshd/down  
  
# Regenerate SSH host keys. Passenger-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
RUN /usr/sbin/enable_insecure_key  
  
# enable nginx  
RUN rm -f /etc/service/nginx/down  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 22  

