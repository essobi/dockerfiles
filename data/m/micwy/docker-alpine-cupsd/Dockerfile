FROM alpine:3.7 as build--cups-epson-escpr  
  
RUN apk add --update --no-cache bash alpine-sdk  
RUN adduser -D -u 1000 -G abuild build  
  
ADD cups-epson-escpr /home/build/cups-epson-escpr  
RUN chown build.abuild /home/build/cups-epson-escpr -R  
  
USER build  
WORKDIR /home/build/cups-epson-escpr  
RUN abuild-keygen -n -a && \  
abuild -r  
  
FROM alpine:3.7  
COPY \--from=build--cups-epson-escpr /home/build/packages/build/x86_64/cups-
epson-escpr-1.6.18-r1.apk /cups-epson-escpr-1.6.18-r1.apk  
  
RUN apk add --update --no-cache cups cups-filters avahi dbus bash && \  
apk add --allow-untrusted /cups-epson-escpr-1.6.18-r1.apk && \  
sed -i 's/#enable-dbus=yes/enable-dbus=no/g' /etc/avahi/avahi-daemon.conf && \  
sed -i 's/Listen localhost:631/Listen 0.0.0.0:631/' /etc/cups/cupsd.conf && \  
sed -i 's/LogLevel warn/LogLevel info/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/>/<Location \/>\n Allow All/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin>/<Location \/admin>\n Allow All\n Require user
@SYSTEM/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin\/conf>/<Location \/admin\/conf>\n Allow All/'
/etc/cups/cupsd.conf && \  
echo "ServerAlias *" >> /etc/cups/cupsd.conf && \  
echo "DefaultEncryption Never" >> /etc/cups/cupsd.conf  
  
ADD https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework
/pipework  
ADD run.sh /run.sh  
RUN chmod 0755 /run.sh  
  
ENV CUPS_ADMIN_USERNAME=admin  
ENV CUPS_ADMIN_PASSWORD=admin  
  
VOLUME /etc/cups/ /etc/avahi/services /var/log/cups /var/spool/cups
/var/spool/cups-pdf /var/cache/cups  
  
EXPOSE 631  
EXPOSE 5353/udp  
  
CMD /run.sh  

