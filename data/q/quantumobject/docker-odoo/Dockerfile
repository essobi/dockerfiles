#name of container: docker-odoo  
#versison of container: 2.1  
FROM quantumobject/docker-baseimage:15.10  
MAINTAINER Angel Rodriguez "angel@quantumobject.com"  
#add repository and update the container  
#Installation of nesesary package/software for this containers...  
RUN echo "deb http://archive.ubuntu.com/ubuntu `cat
/etc/container_environment/DISTRIB_CODENAME`-backports main restricted " >>
/etc/apt/sources.list  
RUN wget -O - https://nightly.odoo.com/odoo.key | apt-key add -  
RUN echo "deb http://nightly.odoo.com/10.0/nightly/deb/ ./" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y -q --force-yes python-software-
properties \  
software-properties-common \  
node-less \  
postgresql \  
odoo \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
# to add postgresqld deamon to runit  
RUN mkdir -p /etc/service/postgresqld /var/log/postgresqld ; sync  
COPY postgresqld.sh /etc/service/postgresqld/run  
RUN chmod +x /etc/service/postgresqld/run \  
&& cp /var/log/cron/config /var/log/postgresqld/ \  
&& chown -R postgres /var/log/postgresqld  
  
# to add odoo deamon to runit  
RUN mkdir -p /etc/service/odoo /var/log/odoo ; sync  
COPY odoo.sh /etc/service/odoo/run  
RUN chmod +x /etc/service/odoo/run \  
&& cp /var/log/cron/config /var/log/odoo/ \  
&& chown -R odoo /var/log/odoo  
  
##startup scripts  
#Pre-config scrip that maybe need to be run one time only when the container
run the first time .. using a flag to don't  
#run it again ... use for conf for service ... when run the first time ...  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
# to allow access from outside of the container to the container service  
# at that ports need to allow access from firewall if need to access it
outside of the server.  
EXPOSE 8069 8070  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

