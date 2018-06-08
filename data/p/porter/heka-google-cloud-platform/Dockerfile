FROM debian:jessie  
RUN apt-get update && apt-get install -y ca-certificates && rm -rf
/var/lib/apt/lists/*  
ADD heka_0.9.1_amd64.deb /tmp/  
RUN dpkg -i /tmp/heka_0.9.1_amd64.deb  
ADD conf /etc/  
ADD docker_log.lua /usr/share/heka/lua_decoders/  
ENTRYPOINT ["hekad"]  

