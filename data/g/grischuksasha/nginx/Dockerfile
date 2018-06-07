FROM nginx:1.13  
RUN apt-get update \  
&& apt-get install -y htop nano git  
  
ADD ./nginx.conf /etc/nginx/  
ADD ./expires.conf /etc/nginx/  
ADD ./cross-domain-fonts.conf /etc/nginx/  
ADD ./cloudflare.conf /etc/nginx/  
ADD ./php-fpm.conf /etc/nginx/  
  
ADD ./conf.d/*.conf /etc/nginx/conf.d/  
  
RUN rm /etc/nginx/conf.d/default.conf  
  
RUN mkdir -p /var/www && chown -R www-data:www-data /var/www  
  
RUN apt-get clean && apt-get autoclean && apt-get autoremove -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["sh", "/entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  
  
WORKDIR /var/www  
  
EXPOSE 80  
EXPOSE 443

