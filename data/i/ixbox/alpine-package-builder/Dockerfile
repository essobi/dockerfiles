FROM alpine:3.7  
RUN apk add --no-cache bash git alpine-sdk py-pip && pip install awscli  
RUN addgroup build && adduser -s /bin/sh -D -G build build && addgroup build
abuild && echo "build ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && sudo -Hu
build abuild-keygen -ain  
RUN mkdir -p /var/cache/distfiles && chmod a+w /var/cache/distfiles && sed -ie
s#/packages/#/packages# /etc/abuild.conf  
  
COPY build.sh build.sh  
  
ENV REPOSITORY https://github.com/alpinelinux/aports.git  
ENV PACKAGES "main/nginx main/nginx-lua"  
CMD [ "/build.sh" ]  

