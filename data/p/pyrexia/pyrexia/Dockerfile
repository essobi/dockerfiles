FROM clojure:lein-2.5.3  
RUN apt-get update && apt-get install -y nginx && apt-get clean && rm -r
/var/lib/apt/lists/*  
COPY project.clj project.clj  
RUN lein deps  
COPY src/ src/  
COPY resources/ resources/  
RUN rm -Rf resources/public/js/compiled  
RUN lein cljsbuild once min  
RUN cp -R resources/public/* /var/www/html  
EXPOSE 80  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
CMD ["nginx", "-g", "daemon off;"]  

