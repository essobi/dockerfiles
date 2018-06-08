# Dockerfile based on lamp container  
FROM tutum/lamp:latest  
MAINTAINER Kevin REMY <kevanescence@hotmail.fr>  
  
ARG commit  
ARG version  
ARG branch  
  
ENV GHOSTYLINK_WEBROOT "/var/www/html/ghostylink"  
ENV DEFAULT_VERSION "v1.4"  
COPY . /image  
  
# Aditional necessary extensions  
RUN chmod u+x -R /image/scripts/ && \  
/image/scripts/install_packages.sh && \  
/image/scripts/get_ghostylink.sh && \  
/image/scripts/install_ghostylink.sh  
  
EXPOSE 80  
CMD ["/image/scripts/entrypoint.sh"]  

