FROM octadesk/node  
  
RUN apt-get install software-properties-common python-software-properties -y  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
  
RUN apt-get -y install nginx make  
  
RUN apt-get install gettext -y  
  
RUN mkdir /srv/www  
  
ADD default /etc/nginx/sites-available/default  
ADD nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80  
  
CMD nginx  

