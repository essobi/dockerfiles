FROM phusion/passenger-customizable:0.9.14  
MAINTAINER Graham Gilbert <graham@pebbleit.com>  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get install -y \  
python-pip \  
python-dev \  
curl  
  
RUN mkdir -p /usr/local  
RUN git clone https://github.com/wdas/reposado.git /usr/local/reposado  
ADD preferences.plist /usr/local/reposado/code/  
ADD reposado.conf /etc/nginx/sites-enabled/reposado.conf  
ADD margarita.conf /etc/nginx/sites-enabled/margarita.conf  
RUN pip install flask  
RUN pip install simplejson  
RUN git clone https://github.com/jessepeterson/margarita.git
/home/app/margarita  
ADD passenger_wsgi.py /home/app/margarita/  
RUN ln -s /usr/local/reposado/code/reposadolib /home/app/margarita/reposadolib  
RUN ln -s /usr/local/reposado/code/preferences.plist
/home/app/margarita/preferences.plist  
RUN rm -f /etc/service/nginx/down  
RUN rm -f /etc/nginx/sites-enabled/default  
VOLUME ["/usr/local/reposado/code/preferences.plist", "/var/www/reposado",
"/etc/nginx/sites-enabled/reposado.conf"]  
  
EXPOSE 80 8089

