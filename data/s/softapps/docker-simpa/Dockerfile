FROM softapps/docker-openerpbase-simpa  
MAINTAINER Arun T K <arun.kalikeri@xxxxxxxx.com>  
ADD additional_addons/pentaho_reports
/opt/odoo/additional_addons/pentaho_reports  
ADD additional_addons/report_webkit /opt/odoo/additional_addons/report_webkit  
ADD additional_addons/web_m2x_options
/opt/odoo/additional_addons/web_m2x_options  
ADD additional_addons/simpa_mobility
/opt/odoo/additional_addons/simpa_mobility  
ADD additional_addons/simpa_network /opt/odoo/additional_addons/simpa_network  
ADD additional_addons/smsclient /opt/odoo/additional_addons/smsclient  
ADD additional_addons/smstemplate /opt/odoo/additional_addons/smstemplate  
  
RUN chown -R odoo:odoo /opt/odoo/additional_addons/  

