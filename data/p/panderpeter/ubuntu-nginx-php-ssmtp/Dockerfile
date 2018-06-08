FROM efaille/nginx-php  
MAINTAINER Peter Pan <panderpeter@mailbox.org>  
  
# Install ssmtp  
RUN apt-get install -y ssmtp  
  
ADD build/ssmtp.conf /etc/ssmtp/ssmtp.conf  
RUN chmod 640 /etc/ssmtp/ssmtp.conf && \  
chown root:www-data /etc/ssmtp/ssmtp.conf  
  
ADD build/ssmtp.sh /root/ssmtpconfig.sh  
RUN chmod +x /root/ssmtpconfig.sh  
  
# Supervisor process  
RUN echo "[program:ssmtpconfig]" > /etc/supervisor/conf.d/ssmtpconfig.conf &&
\  
echo "command=/root/ssmtpconfig.sh" >> /etc/supervisor/conf.d/ssmtpconfig.conf  
  

