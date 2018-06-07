FROM mono:latest  
  
# MAINTAINER Kazuki Yasufuku <wilfrem@gmail.com> # Thanks dude!  
MAINTAINER Cristoffer Fairweather <cfairweather@cfairweather.com>  
  
RUN apt-get update && apt-get install wget unzip sudo && apt-get clean  
  
#add kerman user  
#create home folder  
RUN useradd kerman && mkdir -p /home/kerman  
  
WORKDIR /home/kerman  
RUN wget https://d-mp.org/downloads/release/latest/DMPServer.zip && unzip
DMPServer.zip && rm DMPServer.zip  
  
#change file owner  
RUN mkdir /home/kerman/DMPServer/Universe  
#Copy config files to init proper permissions  
COPY config/*.txt /home/kerman/DMPServer/  
RUN chown -R kerman:kerman /home/kerman  
  
WORKDIR /home/kerman/DMPServer  
  
#run as kerman user  
# USER kerman  
# Run as root and then launch mono as kerman  
#expose DMP port  
EXPOSE 6702  
VOLUME ["/home/kerman/DMPServer/Universe"]  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
# CMD mono /home/kerman/DMPServer/DMPServer.exe  

