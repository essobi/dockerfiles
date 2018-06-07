FROM mono  
  
WORKDIR /opt/eco  
  
RUN apt-get update && apt-get install unzip  
RUN curl https://s3-us-west-2.amazonaws.com/eco-
releases/EcoServer_v0.7.4.6-beta.zip > EcoServer.zip && \  
unzip EcoServer.zip && \  
rm EcoServer.zip  
RUN sed -i 's/"x": 72/"x": 100/' Configs/WorldGenerator.eco && \  
sed -i 's/"y": 72/"y": 100/' Configs/WorldGenerator.eco && \  
sed -i 's/"Password": ""/"Password": ""/' Configs/Network.eco  
  
ENTRYPOINT /usr/bin/mono /opt/eco/EcoServer.exe -nogui  
  

