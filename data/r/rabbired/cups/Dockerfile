FROM debian:testing  
MAINTAINER RedZ  
  
# echo sources.list  
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list  
  
# Install Packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
# Install basic tools and cups  
RUN apt-get install -y sudo locales whois cups cups-client cups-bsd  
# Install all drivers  
RUN apt-get install -y printer-driver-all  
# Install HP drivers  
RUN apt-get install -y hpijs-ppds hp-ppd hplip printer-driver-foo2zjs printer-
driver-fujixerox hpijs-ppds hp-ppd hplip  
ENV DEBIAN_FRONTEND "" LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 LANGUAGE=en_US:en
TZ=Asia/Shanghai  
  
RUN sed -i 's/Listen localhost:631/Listen 0.0.0.0:631/' /etc/cups/cupsd.conf
&& \  
sed -i 's/<Location \/>/<Location \/>\n Allow All/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin>/<Location \/admin>\n Allow All\n Require user
@SYSTEM/' /etc/cups/cupsd.conf && \  
sed -i 's/<Location \/admin\/conf>/<Location \/admin\/conf>\n Allow All/'
/etc/cups/cupsd.conf && \  
echo "ServerAlias *" >> /etc/cups/cupsd.conf && \  
echo "DefaultEncryption Never" >> /etc/cups/cupsd.conf  
  
COPY start-cups.sh /root/start-cups.sh  
RUN chmod +x /root/start-cups.sh  
  
CMD ["/root/start-cups.sh"]  
  
EXPOSE 631  

