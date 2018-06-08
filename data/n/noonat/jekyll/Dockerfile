FROM debian:jessie  
MAINTAINER Nathan Ostgard <noonat@phuce.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y build-essential nginx python-pygments ruby ruby-dev && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/lists && \  
rm /etc/nginx/sites-available/default && \  
rm /etc/nginx/sites-enabled/default && \  
gem install bundler jekyll rake rouge therubyracer  
  
COPY nginx.conf /etc/nginx/conf.d/jekyll.conf  
COPY index.html /opt/site/index.html  
WORKDIR /opt  
  
EXPOSE 80  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  

