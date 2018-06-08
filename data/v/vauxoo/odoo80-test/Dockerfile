FROM vauxoo/odoo-80-image  
MAINTAINER Tulio Ruiz <tulio@vauxoo.com>  
RUN adduser --home=/home/odoo --disabled-password --gecos ""
\--shell=/bin/bash odoo  
RUN echo 'root:odoo' |chpasswd  
RUN mkdir /home/odoo/.ssh  
  
RUN chown odoo:odoo -R /home/odoo  
ADD files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN mkdir /external_files  
ADD files/supervisord.conf /external_files/supervisord.conf  
ADD files/openerp_serverrc /external_files/openerp_serverrc  
USER odoo  
ENV HOME /home/odoo  
ENV ODOO_CONFIG_FILE /home/odoo/.openerp_serverrc  
ENV ODOO_FILESTORE_PATH /home/odoo/.local/share/Odoo/filestore  
  
## Scan the keys to avoid the add question  
RUN ssh-keyscan github.com > /home/odoo/.ssh/known_hosts \  
&& ssh-keyscan launchpad.net >> /home/odoo/.ssh/known_hosts \  
&& ssh-keyscan bitbucket.org >> /home/odoo/.ssh/known_hosts  
  
## Make the instance folder structure  
RUN /bin/bash -c "mkdir -p /home/odoo/instance/{config,extra_addons}"  
RUN cd /home/odoo/instance && git clone -b 8.0 --single-branch --depth=1
https://github.com/Vauxoo/odoo.git odoo  
  
## Add the repos you want to use  
RUN cd /home/odoo/instance/extra_addons \  
&& git clone -b 8.0 --single-branch --depth=1
https://github.com/Vauxoo/addons-vauxoo.git \  
&& git clone -b 8.0 --single-branch --depth=1 https://github.com/OCA/web.git
oca_web  
## Remove the key file you added before  
RUN mkdir -p /home/odoo/.local/share  
ENV XDG_DATA_HOME /home/odoo/.local/share  
ADD files/openerp_serverrc /home/odoo/.openerp_serverrc  
USER root  
RUN mkdir -p /var/log/supervisor  
RUN wget -q -O /entry_point.py
https://raw.githubusercontent.com/vauxoo/docker_entrypoint/master/entry_point.py
\  
&& chmod +x /entry_point.py  
  
## The volumes we want to use  
VOLUME ["/var/log/supervisor", "/home/odoo/.local/share/Odoo", "/tmp",
"/home/odoo/.ssh"]  
  
## Expose xmlrpc and longpolling ports  
EXPOSE 8069  
EXPOSE 8072  
CMD /entry_point.py  

