FROM nginx:latest  
MAINTAINER Junior Lima <josiasjuniorx@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -yf apt-utils python-pip uwsgi uwsgi-plugin-python
dnsutils host git whois  
ENV LANG C.UTF-8  
RUN pip install django requests  
RUN git clone https://github.com/josiasjuniorx/consulta-dominio.git
/var/www/html/  
RUN chmod a+w /var/www/html/static/logs.html  
ADD dominio.conf /etc/nginx/conf.d/default.conf  
ADD whois.conf /etc/whois.conf  
ADD init /init  
EXPOSE 80  
CMD ["/bin/bash", "-c", "source /init"]  

