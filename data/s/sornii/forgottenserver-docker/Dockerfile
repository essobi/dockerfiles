FROM ubuntu:latest  
RUN groupadd -r forgottenserver && useradd -r -g forgottenserver
forgottenserver  
  
RUN apt-get update && apt-get install -y git vim wget cmake build-essential
liblua5.2-dev libgmp3-dev libmysqlclient-dev libboost-system-dev libboost-
iostreams-dev libpugixml-dev  
  
RUN mkdir /home/forgottenserver  
  
EXPOSE 7171  
CMD ["/bin/bash"]  

