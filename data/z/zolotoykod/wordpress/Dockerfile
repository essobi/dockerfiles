FROM zolotoykod/web:latest  
LABEL maintainer="Constantine Karnaukhov <genteelknight@gmail.com>"  
COPY nginx/ /etc/nginx/  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
# Clean working directory of demo files  
ONBUILD RUN rm -rf ./*  

