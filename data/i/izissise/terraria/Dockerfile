# Terraria 1.2.4.1  
# Version latest  
FROM ubuntu  
  
MAINTAINER izissise <morisset.hugues@gmail.com>  
  
RUN apt-get -y update  
  
RUN apt-get -y install wget unzip mono-complete  
  
RUN mkdir tshock && wget
"https://github.com/NyxStudios/TShock/releases/download/v4.3.9/tshock_4.3.9.zip"
-O TShock.zip && unzip TShock.zip -d tshock/  
  
ADD run.sh /  
RUN chmod 755 run.sh  
  
CMD ["./run.sh"]  
  
EXPOSE 7777  

