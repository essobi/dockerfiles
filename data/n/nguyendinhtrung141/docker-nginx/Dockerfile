FROM nginx:alpine  
  
RUN addgroup -g 1000 projadm && adduser -D -G projadm -u 1000 projadm && sed
-i 's/user nginx/user projadm/' /etc/nginx/nginx.conf  

