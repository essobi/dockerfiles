FROM odoo:11.0  
MAINTAINER support@microcom.ca  
  
USER root  
  
# Installing dependances  
RUN pip3 install XLWT phonenumbers pyOpenSSL  
  
#Creating volder for config, addons and logs  
RUN /bin/bash -c "mkdir -p
/opt/odoo/{bin,etc,sources/odoo,additional_addons,data/filestore}" && \  
/bin/bash -c "mkdir -p /opt/odoo/var/{run,log,egg-cache}" && \  
/bin/bash -c "cp -r /var/lib/odoo /opt/odoo/data/" && \  
/bin/bash -c "chmod -R 777 /opt/odoo/data"  
  
# Mount /opt/odoo/data/filestore to allow restoring filestore,
/opt/odoo/additional_addons for users addons and /opt/odoo/etc for config file  
VOLUME ["/opt/odoo/data/filestore", "/opt/odoo/additional_addons",
"/opt/odoo/etc"]  
  
# Expose Odoo services and ssh  
EXPOSE 8069 8071 22  
RUN mkdir /var/run/sshd  
  
# Set default user when running the container  
# USER odoo  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["odoo", "-c", "/opt/odoo/etc/odoo.conf"]  

