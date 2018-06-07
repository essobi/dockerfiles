#  
# Ubuntu Dockerfile  
#  
# https://github.com/koalabz/ubuntu.docker  
#  
# Pull base image  
FROM dockerfile/ubuntu  
MAINTAINER Karim Benbouali <karim.benbouali@koalabz.com>  
  
# Add environment variables scripts  
ADD scripts/environment.sh /usr/local/lib/koalabz/ubuntu/  
ADD scripts/summary.sh /usr/local/lib/koalabz/ubuntu/  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
  
# Define entrypoint and default command  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
CMD ["bash"]  

