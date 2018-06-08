FROM mhart/alpine-node:8  
LABEL maintainer="prasetya@forestcarbon.com"  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
RUN apk add --no-cache gdal  
RUN npm install -g ogre  
EXPOSE 3000  
CMD ["ogre", "-p 3000"]

