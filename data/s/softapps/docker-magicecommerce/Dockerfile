FROM softapps/docker-odoobase-upstream  
MAINTAINER Arun T K <arun.kalikeri@xxxxxxxx.com>  
ADD additional_addons/pentaho_reports
/opt/odoo/additional_addons/pentaho_reports  
ADD additional_addons/attachment_large_object
/opt/odoo/additional_addons/attachment_large_object  
ADD additional_addons/account_financial_report_webkit
/opt/odoo/additional_addons/account_financial_report_webkit  
ADD additional_addons/account_financial_report_webkit_xls
/opt/odoo/additional_addons/account_financial_report_webkit_xls  
ADD additional_addons/magicemart /opt/odoo/additional_addons/magicemart  
ADD additional_addons/product_pricelist_fixed_price
/opt/odoo/additional_addons/product_pricelist_fixed_price  
ADD additional_addons/report_webkit /opt/odoo/additional_addons/report_webkit  
ADD additional_addons/report_xls /opt/odoo/additional_addons/report_xls  
ADD additional_addons/web_m2x_options
/opt/odoo/additional_addons/web_m2x_options  
RUN chown -R odoo:odoo /opt/odoo/additional_addons/  

