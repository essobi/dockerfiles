FROM debian  
MAINTAINER Oleg Morozenkov  
  
RUN apt-get update && \  
apt-get install -y uwsgi-plugin-php php5-curl php5-json && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY uwsgi.conf /etc/uwsgi.conf  
  
EXPOSE 80  
CMD ["uwsgi", "--ini", "/etc/uwsgi.conf"]  

