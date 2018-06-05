############################################################  
# Dockerfile to build a Nagios/Adagios server  
# Based on appcontainers/nagios  
############################################################  
  
FROM centos:6  
  
MAINTAINER Philipp Schmitt <philipp@schmitt.co>  
  
ENV ADAGIOS_HOST adagios.local  
ENV ADAGIOS_USER admin  
ENV ADAGIOS_PASS P@ssw0rd  
  
RUN rpm -ihv http://opensource.is/repo/ok-release.rpm  
RUN yum install -y epel-release  
RUN yum clean all && yum -y update  
  
# Install Nagios, adagios  
RUN yum --enablerepo=ok-testing install -y \  
pnp4nagios mk-livestatus nagios git adagios okconfig acl nagios-plugins-all \  
postfix python-pip  
  
# Install supervisor and supervisor-quick. Service restarts are painfully slow  
# otherwise  
RUN pip install supervisor  
RUN pip install supervisor-quick  
  
# Install build dependencies for nagios-plugins  
# RUN yum -y install aclocal autoheader automake autoconf gcc gettext  
  
# Clone nagios-plugins and install it  
# RUN git clone https://github.com/nagios-plugins/nagios-plugins /tmp/nagios-
plugins  
# RUN cd /tmp/nagios-plugins; \  
# ./configure --prefix=/usr/lib64/nagios --with-cgiurl=http://localhost/nagios
&& \  
# make && make install  
  
# Remove build dependencies for nagios-plugins  
# RUN yum -y uninstall aclocal autoheader automake autoconf gcc gettext && \  
  
# Remove cache and default passwd file  
RUN rm -rf /var/cache/* /etc/nagios/passwd  
  
# Check all permissions  
RUN chown -R nagios /etc/nagios/* && \  
setfacl -R -m group:nagios:rwx /etc/nagios/ && \  
setfacl -R -m d:group:nagios:rwx /etc/nagios/  
  
# Adagios will write to /etc/nagios/adagios, ensure directory exists and  
# nagios.cfg knows about it.  
RUN mkdir -p /etc/nagios/adagios && \  
pynag config --append cfg_dir=/etc/nagios/adagios  
  
# Status view needs broker modules livestatus and pnp4nagios, so configure
nagios.cfg  
RUN pynag config --append "broker_module=/usr/lib64/nagios/brokers/npcdmod.o
config_file=/etc/pnp4nagios/npcd.cfg" && \  
pynag config --append "broker_module=/usr/lib64/mk-livestatus/livestatus.o
/var/spool/nagios/cmd/livestatus" && \  
pynag config --set "process_performance_data=1"  
  
# Add nagios to apache group  
RUN usermod -G apache nagios  
  
# Copy supervisor config over to the container  
COPY supervisord.conf /etc/supervisord.conf  
  
# Copy custom supervisor init.d script (for nagios start|stop)  
COPY nagios-supervisor-wrapper.sh /usr/bin/nagios-supervisor-wrapper.sh  
RUN sed -i 's|^\\(nagios_init_script\\)=\\(.*\\)$|\1="sudo /usr/bin/nagios-
supervisor-wrapper.sh"|g' /etc/adagios/adagios.conf  
RUN echo "nagios ALL=NOPASSWD: /usr/bin/nagios-supervisor-wrapper.sh" >>
/etc/sudoers  
  
# Create childlogdir  
RUN mkdir /var/log/supervisor  
  
# Copy over our custom init script  
COPY run.sh /usr/bin/run.sh  
  
# Make run.sh and supervisor wrapper script executable  
RUN chmod 755 /usr/bin/run.sh /usr/bin/nagios-supervisor-wrapper.sh  
  
WORKDIR /etc/nagios  
  
CMD ["/usr/bin/run.sh"]  
  
EXPOSE 80  
  
VOLUME ["/etc/nagios", "/var/log/nagios"]  

