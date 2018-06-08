FROM base/archlinux  
  
RUN pacman -Syu --noconfirm && pacman -S bash python2-gevent python2-msgpack
python2-pyopenssl --noconfirm  
COPY inits /sbin/inits  
RUN chmod +x /sbin/inits  
RUN mkdir -p /temp && chmod g+ws /temp  
  
WORKDIR /temp  
  
ENTRYPOINT ["/sbin/inits"]  
  
#Expose ports  
EXPOSE 43110 13984  

