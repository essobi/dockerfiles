FROM invenfantasy/scala  
  
# 4 caching  
RUN git clone -b sy https://github.com/invenfantasy/cosmos && cd /cosmos &&
sbt one-jar && \  
cp /cosmos/cosmos-server/target/scala-2.11/cosmos-server_2.11-0.1.5-one-
jar.jar \  
/usr/local/lib/cosmos.jar  
  
WORKDIR /cosmos  

