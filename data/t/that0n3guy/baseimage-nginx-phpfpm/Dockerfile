FROM phusion/baseimage:latest  
MAINTAINER Peter Olson <that0n3guy@users.noreply.github.com>  
  
# Install base packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# Build packages first  
COPY ./packages.sh /build/packages.sh  
RUN /build/packages.sh  
  
COPY ./nginx /build/nginx  
RUN /build/nginx/setup.sh  
  
COPY ./php-fpm /build/php-fpm  
RUN /build/php-fpm/setup.sh  
  
COPY ./composer /build/composer  
RUN /build/composer/setup.sh  
  
# make it so terminal programs worK (like nano)  
RUN echo "export TERM=linux" >> /root/.bashrc  
  
# make errors & access go to terminal  
#RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/sbin/my_init"]  

