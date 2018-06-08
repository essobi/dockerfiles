FROM slitaz/slitaz-base:latest  
  
RUN tazpkg -gi openssh && \  
tazpkg -cc  
  
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed -i 's/#PasswordAuthentication/PasswordAuthentication/'
/etc/ssh/sshd_config  
  
RUN mkdir -p /var/run/sshd  
  
EXPOSE 22/tcp  
  
CMD ["/usr/sbin/sshd", "-D"]  

