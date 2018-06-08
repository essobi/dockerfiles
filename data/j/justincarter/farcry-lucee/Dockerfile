FROM justincarter/lucee-nginx:latest  
  
MAINTAINER Justin Carter justin.w.carter@gmail.com  
  
# configuration  
COPY lucee/lucee-web.xml.cfm /var/www/WEB-INF/lucee/lucee-web.xml.cfm  
COPY nginx/sites-available/default /etc/nginx/sites-available/default  
  
# application code  
COPY farcry /var/www/farcry  

