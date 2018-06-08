FROM node:8.11.1  
RUN npm install svgexport -g --unsafe-perm  
  
RUN apt-get update && apt-get -y install imagemagick bc  
  
COPY converters /usr/local/bin/converters  
ENV PATH="${PATH}:/usr/local/bin/converters"  
RUN chmod +x -R /usr/local/bin/converters  
  
COPY svg-manipulator /usr/local/bin  
RUN chmod +x /usr/local/bin/svg-manipulator  
  
LABEL io.whalebrew.config.volumes
'["$PWD/fonts:/usr/local/share/fonts/type1:ro"]'  
  
ENTRYPOINT [ "svg-manipulator" ]

