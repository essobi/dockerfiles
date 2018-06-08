FROM ubuntu:14.04  
MAINTAINER Jose Tormo Main Informatica @maininformatica jtormo@main-
informatica.com  
  
#  
# Configure APT  
#  
RUN echo deb http://nightly.odoo.com/8.0/nightly/deb/ ./ >
/etc/apt/sources.list.d/odoo-80.list  
RUN apt-get update  
  
#  
# Locale setup  
#  
RUN echo "locales locales/locales_to_be_generated multiselect es_ES.UTF-8
UTF-8" | debconf-set-selections &&\  
echo "locales locales/default_environment_locale select es_ES.UTF-8" |
debconf-set-selections  
RUN apt-get install locales -qq  
RUN locale-gen es_ES.UTF-8  
ENV LC_ALL es_ES.UTF-8  
#  
# Paquetes  
#  
RUN apt-get install --allow-unauthenticated -y supervisor postgresql odoo make
gcc libncurses5-dev bison flex mc joe git openssh-server xfonts-75dpi xfonts-
base xfonts-encodings xfonts-utils  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb && sleep 2 && dpkg -i wkhtmltox-0.12.2.1_linux-trusty-
amd64.deb  
RUN sudo cp /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage  
RUN sudo cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/  
  
#  
# Preparamos el SSH  
#  
RUN mkdir /var/run/sshd  
RUN echo 'root:odooadmin' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
EXPOSE 22  
#  
# PostgreSQL  
#  
COPY ./utf.sql /tmp/utf.sql  
RUN /etc/init.d/postgresql start && su postgres -c "createuser -s odoo" && su
postgres -c "psql postgres < /tmp/utf.sql > /dev/null"  
RUN chown -R postgres.postgres /var/lib/postgresql  
VOLUME ["/var/lib/postgresql"]  
EXPOSE 5432  
#  
# Odoo  
#  
# Localizacion Española  
RUN git clone https://github.com/OCA/l10n-spain.git
/var/lib/odoo/.local/share/Odoo/addons/8.0/  
# Almacenes, Lotes, Albaranes  
# RUN git clone https://github.com/OCA/sale-workflow.git
/var/lib/odoo/.local/share/Odoo/addons/8.0/ --branch 8.0  
RUN chown odoo.odoo /var/lib/odoo/.local/share/Odoo/addons/8.0 -R  
RUN chmod 777 /var/lib/odoo/.local/share/Odoo -R  
RUN sed -i '$d' /etc/odoo/openerp-server.conf  
RUN echo "addons_path = /usr/lib/python2.7/dist-
packages/openerp/addons,/var/lib/odoo/.local/share/Odoo/addons/8.0" >>
/etc/odoo/openerp-server.conf  
RUN sed -i 's/; admin_passwd = admin/admin_passwd = odooadmin/'
/etc/odoo/openerp-server.conf  
EXPOSE 8069  
# Supervisor  
COPY ./supervisord.conf /etc/supervisor/conf.d/maininformatica.conf  
# CMD ["/usr/bin/supervisord", "-n"]  
COPY ./entrypoint.sh /etc/  
RUN chmod a+x /etc/entrypoint.sh  
RUN echo "/etc/entrypoint.sh" >> /root/.bashrc  

