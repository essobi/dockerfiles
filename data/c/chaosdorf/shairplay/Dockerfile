FROM alpine:edge as build  
  
RUN apk add --no-cache gcc autoconf automake musl-dev make libtool libltdl
libao-dev avahi-compat-libdns_sd  
  
RUN mkdir /build  
WORKDIR /build  
COPY . .  
RUN ./autogen.sh  
RUN ./configure  
RUN make  
  
FROM alpine:edge  
  
RUN apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ avahi avahi-compat-libdns_sd
libao pulseaudio-libs avahi-tools openrc dbus  
#RUN ln -s libdns_sd.so.1 /usr/lib/x86_64-linux-gnu/libdns_sd.so  
COPY avahi-daemon.conf /etc/avahi/  
COPY \--from=build /build /build  
CMD /build/run.sh  

