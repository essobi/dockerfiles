FROM alpine  
MAINTAINER lucienchu<lucienchu@hotmail.com>  
  
RUN apk update \  
&& apk upgrade \  
&& apk add ca-certificates git python build-base nodejs curl  
  
WORKDIR /app  
  
RUN echo '{ "allow_root": true }'> ~/.bowerrc  
  
RUN git clone https://github.com/PGBI/kong-dashboard.git \  
&& cd kong-dashboard \  
# chinaland begin  
# && curl --progress --remote-name https://github.com/sass/node-
sass/releases/download/v3.13.0/linux-x64-48_binding.node \  
# && echo "sass_binary_path = /app/kong-dashboard/linux-x64-48_binding.node" >
~/.npmrc \  
# && echo "registry = https://registry.npm.taobao.org" >> ~/.npmrc \  
# chinaland end  
&& npm install \  
&& npm run install  
  
#RUN apk del ca-certificates git python build-base curl  
#RUN rm -rf /app/kong-dashboard/linux-x64-48_binding.node  
COPY docker-entrypoint.sh /tmp  
  
ENTRYPOINT ["/bin/sh", "/tmp/docker-entrypoint.sh"]  
  

