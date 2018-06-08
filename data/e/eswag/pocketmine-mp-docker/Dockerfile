FROM debian:stretch-slim  
  
RUN apt-get update  
RUN apt-get -y install curl sudo  
  
RUN useradd pocketmine  
RUN adduser pocketmine sudo  
WORKDIR /home/pocketmine  
  
ADD server.properties ./server.properties.example  
ADD pocketmine.yml ./pocketmine.yml.example  
  
RUN chown -R pocketmine:pocketmine /home/pocketmine  
  
USER pocketmine  
  
RUN curl -sL https://raw.githubusercontent.com/pmmp/php-build-
scripts/master/installer.sh | bash -s -  
  
USER root  
  
RUN apt-get -y remove curl  
RUN apt-get -y autoremove  
  
ADD entrypoint.sh .  
RUN chmod +x entrypoint.sh  
  
EXPOSE 19132/udp 19132/tcp  
  
CMD ["/home/pocketmine/entrypoint.sh"]  

