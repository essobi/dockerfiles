FROM centos:7.4.1708  
LABEL maintainer="Vitaly Uvarov <v.uvarov@dodopizza.com>"  
  
RUN mkdir /nginx-build  
ADD ./centos-build-nginx.sh /nginx-build/build.sh  
RUN /bin/bash /nginx-build/build.sh && rm -rf /nginx-build/  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
EXPOSE 443  
STOPSIGNAL SIGTERM  
  
CMD ["nginx", "-g", "daemon off;"]

