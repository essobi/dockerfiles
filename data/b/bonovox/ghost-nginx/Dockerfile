FROM ghost  
  
MAINTAINER Carles Sistare <carles.sistare@gmail.com>  
  
RUN apt-get update && \  
apt-get install nginx vim -y && \  
rm /etc/nginx/sites-available/* && \  
rm /etc/nginx/sites-enabled/* && \  
npm install -g forever  
  
RUN echo " \n\  
server { \n\  
listen 0.0.0.0:80; \n\  
server_name _; \n\  
access_log /var/log/nginx/ghost.log; \n\  
location / { \n\  
proxy_set_header X-Real-IP \$remote_addr; \n\  
proxy_set_header HOST \$http_host; \n\  
proxy_set_header X-NginX-Proxy true; \n\  
proxy_pass http://127.0.0.1:2368; \n\  
proxy_redirect off; \n\  
} \n\  
} \n\  
" > /etc/nginx/sites-available/ghost && \  
ln -s /etc/nginx/sites-available/ghost /etc/nginx/sites-enabled/ghost && \  
sed -i 's/exec.*/service nginx start\nservice nginx status\nexec "$@"/g'
/entrypoint.sh  
  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
  
CMD ["npm", "start"]  

