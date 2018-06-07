FROM clouder/clouder-odoo-exec  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
ENV ODOO_CONNECTOR_CHANNELS root:4  
CMD /opt/odoo/files/odoo/openerp-server -c /opt/odoo/etc/odoo.conf
--load=web,web_kanban,connector  

