FROM ursus/ubuntu:latest  
MAINTAINER Djordje Stojanovic <djordje.stojanovic@ursus.rs>  
LABEL vendor="Ursus Software"  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qq -y nginx \  
&& apt-get clean -qq  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i -e "s/user www-data/user root/g" /etc/nginx/nginx.conf  
  
COPY nginx-run.sh /usr/bin/nginx-run  
RUN chmod 775 /usr/bin/nginx-run  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/bin/nginx-run"]

