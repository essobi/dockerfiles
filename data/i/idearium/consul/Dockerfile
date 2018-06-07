FROM smebberson/alpine-consul:3.1.1  
# Remove script that set consul to leave gracefully when container goes down  
# so that when an instance of this container goes up, it can rejoin using the
gossip protocol  
# please refer to https://github.com/hashicorp/consul/issues/750 why we did
this  
RUN rm /etc/cont-finish.d/00-consul  
  
# Copy across the source for the app  
ADD root /  

