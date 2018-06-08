FROM node:latest  
RUN cd /usr/local \  
&& git clone https://github.com/viniciusdacal/socket.io-notify.git socketio\  
&& cd socketio \  
&& npm install  
  
ENV NOTIFICATION_SECRET NOTIFICATION_SECRET  
ENV NOTIFICATION_KEY NOTIFICATION_KEY  
  
VOLUME [ "/usr/local/socketio" ]  
WORKDIR /usr/local/socketio  
  
EXPOSE 3000  
ENTRYPOINT [ "/usr/local/bin/node" ]  
CMD ["/usr/local/socketio/index.js"]  

