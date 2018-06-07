# The FROM instruction sets the Base Image for subsequent instructions. As
such, a valid Dockerfile  
# must have FROM as its first instruction.  
# see https://hub.docker.com/r/smebberson/alpine-nginx/ for available
versions/tags  
FROM nginx:alpine  
  
# The LABEL instruction adds metadata to an image. A LABEL is a key-value
pair.  
# The MAINTAINER instruction sets the Author field of the generated images is
deprecated  
LABEL maintainer Glenn Antoine <me@glennantoine.com>  
  
# The WORKDIR instruction sets the working directory for any RUN, CMD,
ENTRYPOINT, COPY and  
# ADD instructions that follow it in the Dockerfile  
WORKDIR /usr/share/nginx/html  
  
# The ADD instruction copies new files, directories or remote file URLs from
<src>  
# and adds them to the filesystem of the image at the path <dest>  
ADD app2_demosite/ /usr/share/nginx/html  
  
# The EXPOSE instruction informs Docker that the container listens on the
specified network ports  
# at runtime. EXPOSE does not make the ports of the container accessible to
the host.  
EXPOSE 80  

