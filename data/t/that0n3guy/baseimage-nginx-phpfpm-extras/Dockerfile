FROM that0n3guy/baseimage-nginx-phpfpm:latest  
MAINTAINER Peter Olson <that0n3guy@users.noreply.github.com>  
  
# Install base packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
# run our logentries setup script  
COPY ./logentries /build/logentries  
RUN /build/logentries/setup.sh  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/sbin/my_init"]

