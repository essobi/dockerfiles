# VERSION: 0.1  
# DESCRIPTION: Create glide container with its dependencies  
# AUTHOR: Thibault Jamet <thibault.jamet@gmail.com>  
# USAGE:  
# # Build glide image  
# docker build -t glide .  
#  
# # Run the container and mount your source and go directory  
# # requires the go package name in GO_PACKAGE environment variable  
# # do not use the user setting option when running  
# # on windows or mac  
# docker run -it \  
# -u $(id -u):$(id -g) \  
# -v ${HOME}/go:/go \  
# -v ${PWD}:/go/${GO_PACKAGE}\  
# glide  
  
FROM golang:1.6.3-alpine  
  
ARG VERSION=0.11.1-r0  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
apk update && apk add git glide=${VERSION}  
ENTRYPOINT ["glide"]  

