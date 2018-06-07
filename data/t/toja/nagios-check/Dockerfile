FROM jasonrivers/nagios:latest  
MAINTAINER Osvaldo Toja <osvaldo.toja@gmail.com>  
  
ENV NAGIOS_HOME /opt/nagios  
ENV NAGIOS_USER nagios  
ENV NAGIOS_GROUP nagios  
ENV NAGIOS_CMDUSER nagios  
ENV NAGIOS_CMDGROUP nagios  
ENV NAGIOSADMIN_USER nagiosadmin  
ENV NAGIOSADMIN_PASS nagios  
ENV NAGIOS_TIMEZONE UTC  
ENV DEBIAN_FRONTEND noninteractive  
ENV NG_NAGIOS_CONFIG_FILE ${NAGIOS_HOME}/etc/nagios.cfg  
#ENV NG_CGI_DIR ${NAGIOS_HOME}/sbin  
#ENV NG_WWW_DIR ${NAGIOS_HOME}/share/nagiosgraph  
#ENV NG_CGI_URL /cgi-bin  
ADD nagios/nagios.cfg /opt/nagios/etc/nagios.cfg  
ADD nagios/cgi.cfg /opt/nagios/etc/cgi.cfg  
ADD nagios/templates.cfg /opt/nagios/etc/objects/templates.cfg  
ADD nagios/commands.cfg /opt/nagios/etc/objects/commands.cfg  
ADD nagios/localhost.cfg /opt/nagios/etc/objects/localhost.cfg  
  
# Copy example config in-case the user has started with empty var or etc  
#RUN mkdir -p /orig/var && mkdir -p /orig/etc && \  
# cp -Rp /opt/nagios/var/* /orig/var/ && \  
# cp -Rp /opt/nagios/etc/* /orig/etc/  
ADD check.sh /usr/local/bin/check_nagios  
RUN chmod +x /usr/local/bin/check_nagios  
  
VOLUME "/opt/nagios/etc"  
  
CMD [ "/usr/local/bin/check_nagios" ]  

