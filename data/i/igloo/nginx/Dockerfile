FROM ubuntu:16.04  
ENV NGINX_VERSION=1.11.13  
ENV HEADERSMORE_VERSION=0.32  
ENV FILTER_VERSION=0.6.4  
ENV ECHO_VERSION=0.60  
ENV NPS_VERSION=1.11.33.4  
ENV PATH=$PATH:/usr/share/nginx/sbin/  
  
ADD ./install /tmp/nginx-install  
ADD ./install.sh /tmp/install.sh  
  
RUN apt-get -qq update && \  
apt-get -qq install -y wget && \  
cd /tmp/nginx-install  
  
RUN /tmp/install.sh && \  
rm -rf /tmp/nginx-install && \  
rm /tmp/install.sh && \  
cp /etc/nginx/nginx.conf /etc/nginx/conf.d/nginx.conf && \  
echo "include /etc/nginx/conf.d/*.conf;" > /etc/nginx/nginx.conf  
  
ADD ./start.sh /start.sh  
  
VOLUME /etc/nginx/conf.d  
EXPOSE 80 443  
CMD /start.sh  

