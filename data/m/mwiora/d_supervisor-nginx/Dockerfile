from mwiora/d_supervisor  
MAINTAINER Matthias R. Wiora "matthias@wiora.co.uk"  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 \--recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/ubuntu/ $(lsb_release -sc)
nginx" >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y ca-certificates nginx gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
# RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
# && ln -sf /dev/stderr /var/log/nginx/error.log  
  
# prepare to be 3rd-party ready (as needed for hhvm)  
RUN mkdir -p /etc/nginx/sites-enabled/ && mkdir -p /etc/nginx/sites-available/  
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/sites-available/default \  
&& ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
EXPOSE 80 443  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

