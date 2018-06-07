FROM ubuntu:latest  
  
# deps  
RUN apt update -y && apt install -y curl  
  
# Download and extract factorio  
RUN curl -o factorio.tar.gz -L https://www.factorio.com/get-
download/latest/headless/linux64 && tar -xvzf factorio.tar.gz  
  
# expose default port  
EXPOSE 34197  
WORKDIR /factorio/  
  
# copy map or create a new one, simply change the comments around  
# COPY map.zip map.zip  
RUN bin/x64/factorio --create map.zip  
  
# run the factorio server with the map specified  
CMD ["bin/x64/factorio", "--start-server", "map.zip"]  
  
# build with  
# sudo docker build --force-rm -t danielvestol/factorio:latest factorioDocker  
# run with  
# sudo docker run -p 34197:34197 --name factorio -it
danielvestol/factorio:latest  
# to run unattended in the background, do  
# sudo docker run -p 34197:34197 --name factorio -d
danielvestol/factorio:latest

