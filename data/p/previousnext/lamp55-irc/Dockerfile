# This is a docker Drupal environment with stunnel for secure Slack-IRC
integration.  
FROM previousnext/lamp55:latest  
MAINTAINER Peter Lieverdink <peter.lieverdink@previousnext.com.au>  
  
RUN apt-get update -y  
  
##  
# Apache.  
##  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install stunnel4  
  
ADD ./conf/stunnel/slack.conf /etc/stunnel/slack.conf  
ADD ./conf/stunnel/stunnel.pem /etc/stunnel/stunnel.pem  
  
# IRC.  
RUN pear install Net_SmartIRC-1.0.2  
  
# Updated supervisord with stunnel in it.  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
# Inherit everything else from lamp55, ta.  
EXPOSE 22 80  
CMD ["/root/start.sh"]  

