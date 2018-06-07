FROM ubuntu:14.04  
# ubuntu:trusty  
MAINTAINER Hideyuki Takei <takehide22@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
apt-get -yq install software-properties-common --no-install-recommends && \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get update && apt-get upgrade -y && \  
apt-get -yq install nginx --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
COPY nginx.conf /etc/nginx/sites-available/proxy  
RUN ln -s /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy  
  
COPY startup.sh startup.sh  
RUN chmod 744 startup.sh  
  
CMD ["./startup.sh"]  
EXPOSE 5000  

