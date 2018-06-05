FROM maven:latest  
  
RUN wget https://github.com/nats-
io/gnatsd/releases/download/v0.8.0/gnatsd-v0.8.0-linux-amd64.zip -O gnatsd.zip
\  
&& unzip gnatsd.zip \  
&& rm gnatsd.zip  
  
ENV PATH $PATH:/gnatsd-v0.8.0-linux-amd64  
  
RUN wget https://github.com/nats-io/nats-streaming-
server/releases/download/v0.2.0/nats-streaming-server-linux-amd64.zip -O nats-
streaming-server.zip\  
&& unzip nats-streaming-server.zip \  
&& rm nats-streaming-server.zip  
  
ENV PATH $PATH:/nats-streaming-server-linux-amd64  

