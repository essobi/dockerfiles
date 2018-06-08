#########################################################  
## ##  
## _ ##  
## __ _ _ __ __ _(_)_ __ ___ ##  
## / _` | '__/ _` | | '_ \ / _ \ ##  
## | (_| | | | (_| | | | | | __/ ##  
## \\__, |_| \\__,_|_|_| |_|\\___| ##  
## |___/ ##  
## ##  
## ##  
##-----------------------------------------------------##  
## ##  
## Nginx Docker By Mathieu Lescaudron ##  
## ##  
## V 1.0 Created on 24/11/2017 ##  
## ##  
#########################################################  
  
# INTRODUCTION  
#  
# Nginx Alpine ready for automatic-ssl configuration  
  
# BUILD INSTRUCTION  
#  
# docker build -t graine/nginx:latest .  
  
# RUN INSTRUCTION  
#  
# docker run -d -p 80:80 -p 443:443 -v /tmp:/check graine/nginx  
  
FROM nginx:1.13.7-alpine  
  
ADD default.conf /etc/nginx/conf.d/default.conf  
ADD unavailable.html /usr/share/nginx/html/unavailable.html

