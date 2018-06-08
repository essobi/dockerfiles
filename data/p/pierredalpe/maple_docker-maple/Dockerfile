#Starting from the image maintain by Odoo  
FROM xtremxpert/docker-odoo:10.0  
MAINTAINER Benoît "XtremXpert" Vézina <benoit@xtremxpert.com>  
USER root  
COPY rootfs /  
RUN mkdir /mnt/maple-addons && \  
chmod 600 /root/.ssh/id_rsa && \  
chown -R odoo:odoo /etc/odoo && \  
ssh-keyscan git.portall.ca > /root/.ssh/known_hosts && \  
git clone git@git.portall.ca:Maple/web_export_view.git /mnt/maple-
addons/web_export_view && \  
git clone git@git.portall.ca:Maple/siropdelest.git /mnt/maple-
addons/siropdelest && \  
git clone git@git.portall.ca:Maple/maple.git /mnt/maple-addons/maple && \  
git clone git@git.portall.ca:Maple/acer_import.git /mnt/maple-
addons/acer_import && \  
git clone git@git.portall.ca:Maple/stock_picking_from_stock_quants.git
/mnt/maple-addons/stock_picking_from_stock_quants && \  
git clone git@git.portall.ca:Maple/maple_transform.git /mnt/maple-
addons/maple_transform && \  
git clone git@git.portall.ca:Maple/ir_sequence_daily_range.git /mnt/maple-
addons/ir_sequence_daily_range && \  
git clone git@git.portall.ca:Maple/maple_css.git /mnt/maple-addons/maple_css
&& \  
git clone git@git.portall.ca:Maple/barrels_import.git /mnt/maple-
addons/barrels_import && \  
sed -i 's/extra-addons/extra-addons,\/mnt\/maple-addons/g' /etc/odoo/odoo.conf  
USER odoo  

