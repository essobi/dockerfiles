FROM nginx  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
ADD django.conf /etc/nginx/sites-available/django.conf  
ADD uwsgi.conf /etc/nginx/sites-available/uwsgi.conf  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["prod"]  

