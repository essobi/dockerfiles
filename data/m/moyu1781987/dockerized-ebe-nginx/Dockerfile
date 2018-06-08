# Web load balancer Nginx Dockerfile  
FROM nginx:1.11.6  
MAINTAINER Xiaowen Zhang <sean@evestemptation.coml>  
RUN cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup  
COPY ./nginx.conf /etc/nginx/nginx.conf  
  
# install management tools  
Run apt-get update && apt-get install -y \  
htop \  
vim \  
curl \  
wget  
  

