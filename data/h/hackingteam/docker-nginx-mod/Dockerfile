# Date: 2017-11-11  
#  
# Build:  
# docker build -t hackingteam/nginx:1.12.2 .  
#  
# Run:  
# docker run -d -p 80:80 -p 443:443 --name nginx hackingteam/nginx:1.12.2  
#  
FROM ubuntu:16.04  
MAINTAINER HackingTeam "tatdat171@gmail.com"  
RUN apt-get update -qq  
  
COPY build-nginx/build-nginx-ubuntu-16.04_cached.sh /build-nginx.sh  
RUN DEBIAN_FRONTEND=noninteractive bash /build-nginx.sh \  
&& rm /build-nginx.sh  
  
# Make utf-8 enabled by default  
ENV LANG en_US.utf8  
  
COPY nginx-config /etc/nginx  
  
# Forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY ./docker-entrypoint.sh /  
RUN chmod 755 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Define working directory  
WORKDIR /etc/nginx  
  
# Create mount point  
VOLUME ["/etc/nginx", "/etc/letsencrypt"]  
  
# Expose port  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

