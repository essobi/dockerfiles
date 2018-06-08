FROM ruby  
  
RUN gem install minimart  
  
COPY inventory.yml .  
  
ENV MINIMART_URL=minimart.aws.shipwire.com  
ENV MINIMART_PORT=8081  
ENV NGINX_VERSION 1.10.1-1~jessie  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN minimart mirror --load-deps  
  
RUN minimart web --host=http://$MINIMART_URL:$MINIMART_PORT  
  
RUN rm -rf /usr/share/nginx/html  
  
RUN cd /usr/share/nginx && ln -s /web html  
  
EXPOSE 8081  

