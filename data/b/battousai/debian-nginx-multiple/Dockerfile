FROM battousai/debian:latest  
MAINTAINER Mauro Pinto <mauro.s.pinto@gmail.com>  
  
ADD etc/apt /etc/apt  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62
&& \  
apt-get update && \  
apt-get install --no-install-recommends -y nginx && \  
apt-get clean && \  
echo -n > /var/lib/apt/extended_states  
  
RUN rm -rf /etc/nginx/*.d && \  
mkdir -p /etc/nginx/addon.d /etc/nginx/conf.d /etc/nginx/host.d
/etc/nginx/nginx.d  
  
ADD etc/nginx /etc/nginx  
ADD config /config  
ADD supervisord.conf /etc/supervisor/conf.d/nginx.conf  
EXPOSE 80  

