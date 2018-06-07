FROM qrry/dynamic-proxy:latest  
  
ADD redirects.conf /etc/nginx/conf.d/  
ADD users.conf /etc/nginx/conf.d/  
  
RUN mkdir -p /etc/ssl/private  
RUN ln -sf /etc/letsencrypt/live/underdogma.net/fullchain.pem
/etc/ssl/private/  
RUN ln -sf /etc/letsencrypt/live/underdogma.net/privkey.pem /etc/ssl/private/  

