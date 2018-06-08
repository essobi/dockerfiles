FROM php:7.1.15-cli  
  
RUN mkdir -p /opt/ypoirier  
COPY script.php /opt/ypoirier  
COPY scriptchase.php /opt/ypoirier  
COPY task.sh /opt/ypoirier  
RUN apt-get update && \  
apt-get install -y ssmtp && \  
apt-get clean && \  
echo "FromLineOverride=YES" >> /etc/ssmtp/ssmtp.conf && \  
sed -i -e "s#mailhub=mail#mailhub=mail.uqam.ca#" /etc/ssmtp/ssmtp.conf && \  
echo 'sendmail_path = "/usr/sbin/ssmtp -t"' >
/usr/local/etc/php/conf.d/mail.ini  
  
CMD [ "bash", "/opt/ypoirier/task.sh" ]  

