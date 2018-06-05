FROM albertalvarezbruned/odoo:base  
  
RUN curl -fsSL
http://nightly.odoo.com/old/openerp-6.1/6.1.0/openerp_6.1-1-1_all.deb -o
/tmp/open.deb  
  
RUN chmod +x /tmp/open.deb  
RUN dpkg --force-depends -i /tmp/open.deb  
RUN apt-get update  
RUN apt-get -y install -f --no-install-recommends  
RUN rm -rf /var/lib/apt/lists/* /tmp/open.deb  
  
RUN mkdir -p /home/odoo  
WORKDIR /home/odoo  
RUN useradd odoo -u 1000 -s /bin/bash  
RUN chown odoo -R /home/odoo  
ENV HOME /home/odoo  
RUN chown -R odoo /addons  
RUN chown odoo /etc/odoo/openerp-server.conf  
RUN mkdir -p /mnt/extra-addons \  
&& chown -R odoo /mnt/extra-addons  
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]  
EXPOSE 8069 8071  
ENV OPENERP_SERVER /etc/odoo/openerp-server.conf  
USER odoo  
  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["openerp-server"]  

