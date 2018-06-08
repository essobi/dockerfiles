FROM debian:wheezy  
  
RUN apt-get update \  
&& apt-get install -y ca-certificates nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
EXPOSE 80 443  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
CMD ["nginx", "-g", "daemon off;"]

