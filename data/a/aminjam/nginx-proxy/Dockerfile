FROM scratch  
MAINTAINER Amin Jams <aminjam@outlook.com>  
  
ADD ./rootfs.tar /  
ADD ./rootfs/busybox/opkg.conf /etc/opkg.conf  
ADD ./rootfs/busybox/opkg-install /usr/bin/opkg-install  
ADD ./rootfs/busybox/functions.sh /lib/functions.sh  
RUN opkg-cl install
http://downloads.openwrt.org/snapshots/trunk/x86_64/packages/base/libgcc_4.8-linaro-1_x86_64.ipk  
RUN opkg-cl install
http://downloads.openwrt.org/snapshots/trunk/x86_64/packages/base/libc_0.9.33.2-1_x86_64.ipk  
RUN chmod +x /usr/bin/opkg-install  
RUN opkg-install bash && rm -rf /var/opkg-lists  
RUN mkdir -p /var/lib/nginx  
  
ADD ./stage/* /usr/bin/  
RUN chmod +x /usr/bin/*  
  
RUN mkdir /etc/nginx/sites-enabled  
RUN mkdir /home/app  
RUN rm /etc/nginx/nginx.conf /etc/nginx/mime.types  
ADD ./app-config/nginx.conf /etc/nginx/nginx.conf  
ADD ./app-config/mime.types /etc/nginx/mime.types  
ADD ./app-config/proxy_params /etc/nginx/proxy_params  
Add ./app-config/Procfile /home/app/Procfile  
Add ./app-config/nginx.tmpl /home/app/nginx.tmpl  
##################### INSTALLATION END #####################  
RUN echo 'nginx:' `nginx -v`  
EXPOSE 80  
ENV DOCKER_HOST unix:///tmp/docker.sock  
WORKDIR /home/app  
CMD ["forego", "start", "-r"]  

