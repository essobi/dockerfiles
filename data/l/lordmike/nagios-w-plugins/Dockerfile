FROM jasonrivers/nagios:latest  
  
MAINTAINER Michael Bisbjerg <michael@mbwarez.dk>  
  
# Add std. plugins  
RUN apt-get update && \  
apt-get install -y nagios-plugins && \  
rm -rf /var/cache/apk/*  
  
# Add scripts  
COPY Scripts/check_sslscan.pl /opt/nagios/libexec/check_sslscan  
  
RUN chmod +x /opt/nagios/libexec/check_sslscan

