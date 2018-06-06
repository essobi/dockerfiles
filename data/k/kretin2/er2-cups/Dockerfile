############################################################  
# Based on Debian Streaaaaaaaaaaaaaaaaaaåtch  
############################################################  
  
FROM centos:latest  
  
MAINTAINER Keaton Burleson keaton.burleson@me.com  
  
EXPOSE 631  
  
VOLUME /var/log/cups /var/run/cups  
  
############################################################  
# Arguments  
############################################################  
ENV WK_URL
https://bitbucket.org/wkhtmltopdf/wkhtmltopdf/downloads/wkhtmltox-0.13.0-alpha-7b36694_linux-
centos7-amd64.rpm  
  
############################################################  
# Install Essential Packages  
############################################################  
RUN yum -y install cups hostname xorg-x11-server-Xvfb libpng libjpeg openssl
icu libXrender && \  
yum -y install xorg-x11-fonts-Type1 xorg-x11-fonts-75dpi wget && \  
yum -y --setopt tsflags= reinstall cups && \  
yum clean all  
  
############################################################  
# Install WKHTMLTOPDF  
############################################################  
  
RUN wget $WK_URL  
RUN rpm -ivh wkhtmltox*.rpm  
  
CMD /usr/bin/Xvfb :42 -screen 0 1024x768x24 -ac +extension GLX +render
-noreset  
  
  
############################################################  
# Configure  
############################################################  
COPY scripts/wkhtmltopdf.sh /usr/local/sbin/html2pdf  
COPY scripts/xvfb-run /usr/bin/xvfb-run  
COPY conf/cupsd.permissive.conf /etc/cups/cupsd.conf  
  
CMD ["cupsd", "-f"]  
  

