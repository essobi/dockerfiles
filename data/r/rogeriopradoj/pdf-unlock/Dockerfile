FROM debian:latest  
  
MAINTAINER rogeriopradoj <rogeriopradoj@gmail.com>  
  
RUN apt-get update  
  
RUN apt-get install pdftk -y \  
&& apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

