FROM debian:jessie  
MAINTAINER Antoine Millet <antoine@inaps.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install python nginx-full \  
&& apt-get clean  
  
RUN mkdir /nginx && chmod 777 /nginx  
  
ADD launcher.py /  
RUN chmod +x /launcher.py  
  
ADD nginx.conf /default_nginx.conf  
  
EXPOSE 80  
VOLUME /nginx  
  
CMD []  
ENTRYPOINT ["/launcher.py"]  

