FROM nginx  
  
RUN apt-get -y update; apt-get -y install nginx-nr-agent  
  
CMD nginx -g 'deamon off;' && service nginx-nr-agent start

