#FROM hypriot/rpi-node:slim  
FROM node:latest  
  
RUN mkdir /app  
  
# expose volume  
VOLUME /data  
  
# setup external volume for script  
RUN apt-get update ;\  
apt-get install python ;\  
wget -O /app/speedtest-cli https://raw.github.com/sivel/speedtest-
cli/master/speedtest_cli.py ;\  
chmod +x /app/speedtest-cli ;\  
touch /data/speeds.csv  
  
# set the working dear to the app  
WORKDIR /app  
# install node packages / copy all source files  
ADD package.json /app/package.json  
COPY src/ /app/  
RUN cd /app && npm install  
  
# setup script  
# RUN python /app/measure.py  
# expose port for server  
EXPOSE 80  
# start the server as entry point  
ENTRYPOINT ["/bin/bash", "start.sh"]  
#ENTRYPOINT ["python", "measure.py"]  

