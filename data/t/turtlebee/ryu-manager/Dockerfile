FROM osrg/ryu:latest  
  
LABEL maintainer="Fu-Lian Wong <turtle11311@gmail.com>"  
ENV HOME /root  
ENV PYTHONPATH /root/ryu  
  
WORKDIR /root/ryu  
EXPOSE 6633 8080  
RUN mkdir /root/ryu/custom && touch /root/ryu/custom/__init__.py  
  
VOLUME [ "/root/ryu/custom" ]  
  
ENTRYPOINT [ "ryu-manager" ]  
CMD [ "ryu.app.ofctl_rest", "ryu.app.rest_vtep", "ryu.app.simple_switch_13" ]  

