## xlmp  
FROM xenocider/container:python3.5.2  
LABEL maintainer="xenos <xenos.lu@gmail.com>"  
  
# dumb-init \  
# runit \  
# supervisor \  
RUN apk add --no-cache \  
git \  
nginx \  
s6 &&\  
pip3 install tornado==4.5.3 &&\  
pip3 install xmltodict==0.11.0 &&\  
mkdir /run/nginx &&\  
rm -f /etc/nginx/conf.d/default.conf  
  
# copy nginx config file  
COPY xlmp.conf /etc/nginx/conf.d/  
  
# deploy script  
COPY deploy /usr/local/bin  
RUN chmod +x /usr/local/bin/deploy  
  
# git clone  
RUN git clone https://github.com/XenosLu/xlmp.git /xlmp  
  
EXPOSE 80  
# media folder:  
# VOLUME /xlmp/media  
RUN chmod -R +x /xlmp/docker/s6  
# ENTRYPOINT ["/bin/sh", "/xlmp/docker/docker-entrypoint.sh"]  
# CMD ["/usr/bin/supervisord", "-c", "/xlmp/docker/supervisord.conf"]  
# CMD ["/usr/bin/dumb-init", "/bin/sh", "/xlmp/docker/init"]  
CMD ["/bin/s6-svscan", "/xlmp/docker/s6/"]  

