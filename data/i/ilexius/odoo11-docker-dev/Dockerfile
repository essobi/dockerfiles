FROM ilexius/odoo11-ubuntu-base:8.0  
MAINTAINER ilexius GmbH <info@ilexius.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG=C.UTF-8  
RUN useradd odoo -d /srv/odoo -m  
RUN mkdir /var/lib/odoo  
RUN chown odoo:odoo /var/lib/odoo  
RUN mkdir /srv/odoo-addons  
RUN chown odoo:odoo /srv/odoo-addons  
  
COPY run.py /  
COPY odoo.conf.template /srv/  
  
RUN chmod 755 /run.py  
  
# Expose Odoo services  
EXPOSE 8069 8071  
# Set the default config file  
ENV ODOO_RC /etc/odoo/odoo.conf  
  
# Set default user when running the container  
USER odoo  
  
CMD ["python", "/run.py"]  

