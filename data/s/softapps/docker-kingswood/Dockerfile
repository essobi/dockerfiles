#Inspiration 1: DotCloud  
#Inspiration 2: https://github.com/justnidleguy/  
#Inspiration 3: https://bitbucket.org/xcgd/ubuntu4b  
FROM softapps/docker-openerpbase-kings  
MAINTAINER Arun T K <arun.kalikeri@xxxxxxxx.com>  
  
  
ADD . /pd_build  
  
RUN /pd_build/install.sh  
  
# Execution environment  
USER 0  
VOLUME ["/opt/odoo/var", "/opt/odoo/etc", "/opt/odoo/additional_addons",
"/opt/odoo/data"]  
  
# Set the default entrypoint (non overridable) to run when starting the
container  
ENTRYPOINT ["/app/bin/boot"]  
CMD ["help"]  

