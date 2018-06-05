# Dockerfile for Lucee on Tomcat  
# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.16  
MAINTAINER Dennis Clark <boomfish@gmail.com>  
  
ENV LUCEE_INSTALLER_URL
http://railo.viviotech.net/downloader.cfm/id/133/file/lucee-4.5.1.000-pl0-linux-x64-installer.run  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Download installer, run it, and delete it in one step to avoid committing
the installer in a FS layer  
RUN curl $LUCEE_INSTALLER_URL -o /root/lucee-installer && \  
chmod u+x /root/lucee-installer && \  
/root/lucee-installer --mode unattended --railopass docker --installconn false
\--startatboot false && \  
rm -rf /root/lucee-installer /tmp/*  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Apache Tomcat Native Library (for Tomcat performance) and Python
Jinja2 and Perl Template Toolkit (for config templates)  
RUN add-apt-repository ppa:pharmgkb/trusty && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
libtcnative-1 \  
python-pip \  
python-jinja2 \  
libtemplate-perl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install envtpl command-line tool for Jinja2  
RUN pip install envtpl  
  
# Add custom Tomcat setenv.sh script  
COPY setenv.sh /opt/lucee/tomcat/bin/  
RUN chmod 755 /opt/lucee/tomcat/bin/setenv.sh  
  
# Custom server.xml that treats /opt/lucee/tomcat/webapps/ROOT/ as the default
application (ie. matches any hostname)  
COPY server.xml /opt/lucee/tomcat/conf/  
  
# Relocate Railo config for default site to /opt/lucee/config/web/ROOT  
COPY web.xml /opt/lucee/tomcat/webapps/ROOT/WEB-INF/web.xml  
RUN mkdir -p /opt/lucee/config/web && mv /opt/lucee/tomcat/webapps/ROOT/WEB-
INF/lucee /opt/lucee/config/web/ROOT  
  
# Add custom version of tpage that reads environment variables  
COPY tpage2.pl /usr/local/bin/tpage2  
RUN chmod 755 /usr/local/bin/tpage2  
  
# Setup my_init run script  
COPY run.sh /etc/service/lucee/run  
RUN chmod 700 /etc/service/lucee/run  
  
# Setup my_init setup script to configure Railo  
COPY setup_lucee.sh /etc/my_init.d/50_setup_lucee.sh  
RUN chmod 755 /etc/my_init.d/50_setup_lucee.sh  
  
# Copy default templates  
COPY includes/ /opt/lucee/config/includes/  
  
# Run the setup script now so that the compiled templates are baked into the
image  
RUN /etc/my_init.d/50_setup_lucee.sh  
  
# Lucee server and web admin password hashes default to 'docker' (CHANGEME!)  
ENV LUCEE_SERVER_ADMIN_PASSWORD_HSPW
82932827b6ba3c390e001326b8b6ad2140bf8b64ea1bf2c52103e58b27a5532b  
ENV LUCEE_SERVER_ADMIN_PASSWORD_SALT "CFF5496C-C950-4D39-A07927563C74D733"  
ENV LUCEE_WEB_ADMIN_PASSWORD_HSPW
33600d803cdfe865c5aff0a403a60d0c11ee94697f34f5a13145a5223874b112  
ENV LUCEE_WEB_ADMIN_PASSWORD_SALT "DFF154CD-7BE8-4A10-8A1A8ECAA01A00EA"  
# Expose connector ports (8888 = HTTP 1.1, 8009 = AJP 1.3)  
EXPOSE 8888 8009  
# Delete the default application files when using this as a base image  
ONBUILD RUN rm -rf /opt/lucee/tomcat/webapps/ROOT/Application.cfc
/opt/lucee/tomcat/webapps/ROOT/favicon.ico
/opt/lucee/tomcat/webapps/ROOT/index.cfm /opt/lucee/tomcat/webapps/ROOT/assets  
  
# Uncomment this if you want to enable SSH, required for 'vagrant ssh' to work  
#RUN rm -f /etc/service/sshd/down  

