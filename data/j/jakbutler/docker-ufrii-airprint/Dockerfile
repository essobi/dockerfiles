FROM aadl/cups:latest  
  
MAINTAINER jakbutler  
  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
ENV DRIVER_URL='http://gdlp01.c-wss.com/gds/6/0100009236/01/linux-UFRII-
drv-v350-usen.tar.gz'  
ENV AIRPRINT_GENERATE_URL='https://raw.github.com/tjfontaine/airprint-
generate/master/airprint-generate.py'  
# ENV CUPS_USER_ADMIN=admin  
# ENV CUPS_USER_PASSWORD=secr3t  
  
#########################################  
## DEPENDENCY INSTALL ##  
#########################################  
# Base AADL image installs cups (2.2.1), cups-filters, cups-pdf, and whois  
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get -y install \  
autoconf \  
automake \  
curl \  
inotify-tools \  
libglade2-0 \  
libpango1.0-0 \  
libpng16-16 \  
python-cups \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# TODO: Install golang and google-cloud-print  
  
#########################################  
## CUPS Config ##  
#########################################  
COPY cups/cupsd.conf /etc/cups/cupsd.conf  
  
#########################################  
## Script Setup ##  
#########################################  
RUN rm /root/start_cups.sh  
COPY start-cups.sh /root/start-cups.sh  
RUN chmod +x /root/start-cups.sh  
COPY printer-update.sh /root/printer-update.sh  
RUN chmod +x /root/printer-update.sh  
  
## Install and configure AirPrint  
RUN wget --no-check-certificate $AIRPRINT_GENERATE_URL -P /root/  
RUN chmod +x /root/airprint-generate.py  
  
## Add proper mimetypes for iOS  
COPY mime/airprint.convs /share/cups/mime/airprint.convs  
COPY mime/airprint.types /share/cups/mime/airprint.types  
  
## Install Canon URFII drivers  
# RUN touch /var/lib/dpkg/status  
#&& cp /var/lib/dpkg/available-old /var/lib/dpkg/available  
RUN curl $DRIVER_URL | tar xz  
RUN dpkg -i *-UFRII-*/64-bit_Driver/Debian/*common*.deb  
RUN dpkg -i *-UFRII-*/64-bit_Driver/Debian/*ufr2*.deb  
RUN dpkg -i *-UFRII-*/64-bit_Driver/Debian/*utility*.deb  
RUN rm -rf *-UFRII-*  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
VOLUME /etc/cups/ \  
/etc/avahi/services/ \  
/var/log/cups \  
/var/spool/cups \  
/var/spool/cups-pdf \  
/var/cache/cups  
# /var/run/dbus  
  
#########################################  
## Startup Command ##  
#########################################  
CMD ["/root/start-cups.sh"]  
  
#########################################  
## PORTS ##  
#########################################  
EXPOSE 631

