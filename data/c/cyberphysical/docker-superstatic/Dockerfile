FROM bradrydzewski/node:0.10  
RUN /home/ubuntu/nvm/v0.10.22/bin/npm install -g bower grunt-cli karma
superstatic  
  
RUN sudo curl -sLo /usr/local/bin/ep
https://github.com/kreuzwerker/envplate/releases/download/v0.0.5/ep-linux &&
sudo chmod +x /usr/local/bin/ep  
  
WORKDIR /app  
EXPOSE 8080  
CMD ["/usr/local/bin/ep", "/app/.env.json", "--",
"/usr/local/bin/superstatic", "--port","8080","--host","0.0.0.0", "--gzip"]

