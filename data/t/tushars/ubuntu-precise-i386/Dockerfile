###--------------------------------------------------###  
### Docker Image by tushars @ TechPeek ###  
###--------------------------------------------------###  
  
FROM scratch  
  
# File Author / Maintainer  
MAINTAINER Tushar Sakhadeo  
  
# debootstrap build custom base image with basic packages dumb-init,
supervisord, sshd, vim  
ADD ubuntu-precise-i386.tgz /  
  
# Define working directory.  
WORKDIR /root  
  
# Expose ssh port  
EXPOSE 22  
  
# Runs "/usr/local/bin/dumb-init -- /my/script --with --args"  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
  
# Default command  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

