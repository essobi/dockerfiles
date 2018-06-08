FROM centos:7  
MAINTAINER Vladimir Bueb "vlord@free.fr"  
RUN yum -y update  
RUN yum -y install epel-release  
RUN yum -y localinstall https://labs.consol.de/repo/stable/rhel7/x86_64/labs-
consol-stable.rhel7.noarch.rpm  
RUN yum -y install naemon  
RUN yum -y install mailx exim  
RUN yum -y install nagios-plugins nagios-plugins-all nagios-plugins-nrpe nrpe  
RUN yum -y install supervisor  
RUN sed -i -e 's/begin rewrite/begin rewrite\n.include
\/etc\/exim\/rewrite.conf/g' /etc/exim/exim.conf  
RUN cp -r /etc/naemon/conf.d /etc/naemon/conf.d.default  
RUN cp /etc/thruk/cgi.cfg /etc/thruk/cgi.cfg.default  
COPY naemon.ini /etc/supervisord.d/naemon.ini  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/bin/supervisord"]  

