FROM ubuntu:14.04  
MAINTAINER "Christian Kniep <christian@qnib.org>"  
RUN echo "2015-10-14.1";apt-get update && \  
apt-get install -y supervisor && \  
echo "supervisord -c /etc/supervisord.conf" >> /root/.bash_history && \  
echo "supervisorctl status" >> /root/.bash_history && \  
echo "tail -f /var/log/supervisor/" >> /root/.bash_history  
ADD etc/supervisord.conf /etc/supervisord.conf  
  
RUN echo "/usr/bin/supervisord -c /etc/supervisord.conf" >>
/root/.bash_history  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  
  

