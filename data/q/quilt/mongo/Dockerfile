FROM mongo:3.2  
  
COPY start.go /  
  
RUN apt-get -y update \  
&& apt-get install -y golang-go iputils-ping\  
&& go build /start.go \  
&& apt-get remove \--purge -y golang-go \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/start"]  

