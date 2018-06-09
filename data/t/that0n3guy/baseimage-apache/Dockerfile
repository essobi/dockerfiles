FROM phusion/baseimage:latest  
MAINTAINER Peter Olson <that0n3guy@users.noreply.github.com>  
  
# Install base packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# Build packages first  
COPY ./packages.sh /build/packages.sh  
RUN /build/packages.sh  
  
COPY ./apache /build/apache  
RUN /build/apache/setup.sh  
  
COPY ./composer /build/composer  
RUN /build/composer/setup.sh  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/sbin/my_init"]

