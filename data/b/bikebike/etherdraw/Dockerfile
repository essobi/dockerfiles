# etherdraw #  
# node 9.2  
FROM node:9-alpine  
MAINTAINER Jonathan Rosenbaum <fspc@freesoftwarepc.com>  
  
RUN apk update; apk add bash git giflib-dev libjpeg-turbo-dev curl mysql-
client python2 pkgconfig cairo-dev make g++  
  
WORKDIR /opt/  
  
RUN git clone git://github.com/JohnMcLear/draw.git  
  
ENV PYTHON=/usr/bin/python2  
  
WORKDIR draw  
  
RUN bin/installDeps.sh && rm settings.json  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN sed -i 's/^node/exec\ node/' bin/run.sh  
  
VOLUME /opt/draw/var /opt/draw/node_module  
RUN ln -s var/settings.json settings.json  
  
EXPOSE 9002  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bin/run.sh", "--root"]  

