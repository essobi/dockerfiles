FROM debian:jessie  
  
ADD rootfs /  
  
RUN /install.sh && /configure.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
  
CMD [ "mapcrafter" "-b", "-c", "/etc/mapcrafter/render.conf" ]  

