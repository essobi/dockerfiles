# Setting the base to docker-node-unoconv:8.11.1  
FROM telemark/docker-node-
unoconv:8.11.2@sha256:a0ccd23cec011eb679b5b8f32f068193133f008fed1f2acfb7f279d8793eb1fd  
  
#### Begin setup ####  
# Installs git and make utils  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y make
gcc g++ python && apt-get clean  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Startup  
ENTRYPOINT sh start.sh  

