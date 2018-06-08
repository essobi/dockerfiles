FROM patterns/x11vnc  
  
MAINTAINER 興怡  
ENV PROJ_DIR /home/alpine/surf-2.0  
  
RUN apk --no-cache add curl make gcc musl-dev linux-headers \  
build-base abuild binutils cmake extra-cmake-modules \  
tar gzip ccache gtk+3.0-dev webkit2gtk-dev \  
gtk+3.0 webkit2gtk \  
dbus mesa-dri-swrast \  
&& curl -L http://dl.suckless.org/surf/surf-2.0.tar.gz \  
| tar xz -C /home/alpine \  
&& cd $PROJ_DIR \  
&& make clean install \  
&& apk del make gcc musl-dev linux-headers \  
build-base abuild binutils cmake extra-cmake-modules \  
tar gzip ccache gtk+3.0-dev webkit2gtk-dev \  
&& rm -rf /apk /tmp/* /var/cache/apk/* $PROJ_DIR \  
  
USER alpine  
  

