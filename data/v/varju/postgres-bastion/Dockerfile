FROM postgres  
MAINTAINER Alex Varju <alex@varju.ca>  
  
RUN apt-get update \  
&& apt-get install -y openssh-server  
  
COPY start /  
  
EXPOSE 22  
CMD ["/start"]  

