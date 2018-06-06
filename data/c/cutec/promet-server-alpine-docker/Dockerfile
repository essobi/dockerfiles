FROM alpine  
RUN apk add --no-cache bash wget tar gcc xz postgresql-client mysql-client
sqlite nano gdk-pixbuf glib gtk+2.0 xvfb  
RUN wget http://downloads.free-erp.de/promet-erp-
services_7.0.439_amd64-gtk2.deb --level=25839  
RUN ar p promet-erp-services_7.0.439_amd64-gtk2.deb data.tar.xz | tar -xJ && \  
rm promet-erp-services_7.0.439_amd64-gtk2.deb && \  
apk del wget tar gcc xz  
#RUN ls /usr/lib  
#RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2 <\- dont work, lazarus applications needs standard libc  
EXPOSE 8085  
VOLUME ["/usr/lib/promet-erp/web"]  
COPY entrypoint.sh /opt/entrypoint.sh  
RUN ["chmod", "+x", "/opt/entrypoint.sh"]  
ENTRYPOINT ["/opt/entrypoint.sh"]  

