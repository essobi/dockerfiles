FROM nginx:latest  
MAINTAINER Filipe Silva <silvam.filipe@gmail.com>  
  
# Install Jinja for template usage  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -y -q \  
build-essential \  
curl \  
python2.7 \  
python2.7-dev \  
python-pip && \  
pip install --upgrade pip virtualenv && \  
pip install Jinja2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY etc /etc/nginx_extras  
RUN rm -rf /etc/nginx && \  
mv /etc/nginx_extras /etc/nginx && \  
mkdir -p /etc/nginx/sites-enabled  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

