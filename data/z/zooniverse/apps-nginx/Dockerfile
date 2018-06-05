FROM zooniverse/nginx  
  
RUN apt-get update && apt-get install -y python3 python3-requests  
  
RUN mkdir -p /etc/nginx-sites/ && touch /etc/nginx-deny.conf  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD start.sh /  
ADD gen-cf-conf.py /  
  
ENTRYPOINT /start.sh  

