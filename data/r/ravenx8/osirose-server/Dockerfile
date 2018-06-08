# Build the Target Server  
FROM ravenx8/ubuntu-dev as build  
WORKDIR /  
  
RUN git clone https://github.com/dev-osrose/osIROSE-new.git  
  
WORKDIR /osIROSE-new  
RUN git submodule update --init --recursive  
  
RUN mkdir /build  
WORKDIR /build  
RUN CC=gcc-7 CXX=g++-7 cmake -DOFFICIAL_BUILD=ON /osIROSE-new \  
&& CC=gcc-7 CXX=g++-7 cmake --build . --config ${build_config:-Release} \  
&& mkdir /server \  
&& cp -r /build/bin/* /server \  
&& cp /osIROSE-new/cmake/scripts/docker_start_server.sh /server/start.sh  
RUN chmod -R 777 /server/  
  
# Run the final output  
FROM ubuntu:artful  
COPY \--from=build /server/ /  
  
RUN apt-get update && apt-get install -y libmysqlclient-dev libcurl4-gnutls-
dev  
  
ARG CONFIG_FILE=/config/server.json  
ARG SERVER=LoginServer  
  
ENV CONFIG_FILE $CONFIG_FILE  
ENV SERVER $SERVER  
  
VOLUME ["/data"]  
VOLUME ["/config"]  
VOLUME ["/symbols"]  
  
# Default Server client port  
EXPOSE 29000 29100 29200  
# Default ISC Server port  
EXPOSE 29010 29110 29210  
ENTRYPOINT [ "/start.sh" ]  

