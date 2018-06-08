FROM kdvn/ubuntu  
  
RUN mkdir -p /mnt/extra-addons /mnt/oefilestore /opt/oe7 /opt/workspace  
  
#RUN wget -qO- http://10.10.0.1/openerp_7.0.latest.tar.gz | tar xz -C
/opt/oe7/ --owner=openerp --strip 1  
RUN wget -qO-
http://nightly.odoo.com/7.0/nightly/src/openerp_7.0.latest.tar.gz | tar xz -C
/opt/oe7/ --strip 1  
  
RUN adduser -u 1000 --system --group --home /home/openerp --shell /bin/bash
openerp  
  
RUN echo "openerp ALL = NOPASSWD : /usr/bin/tee , /bin/sed , /usr/bin/apt-get
, /usr/bin/aptitude , /usr/sbin/usermod " | tee -a /etc/sudoers  
  
RUN mkdir -p /home/openerp  
  
ENV OPENERP_SERVER /etc/openerp/openerp-server.conf  
  
VOLUME ["/mnt/oefilestore", "/mnt/extra-addons"]  
  
RUN chown -R openerp /mnt/extra-addons /mnt/oefilestore /opt/oe7 /home/openerp  
RUN chown -R :9900 /home/openerp  
EXPOSE 8069  
# Copy entrypoint script and Odoo configuration file  
COPY ./entrypoint.sh /  
COPY ./openerp-server.conf /etc/openerp/  
USER openerp  
WORKDIR /opt/workspace  
  
ENV PATH "$PATH:/opt/oe7"  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/opt/oe7/openerp-server"]  

