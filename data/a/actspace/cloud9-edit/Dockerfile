FROM node:6.11.2  
# Install Cloud9 IDE  
RUN git clone git://github.com/c9/core.git /c9sdk  
WORKDIR /c9sdk  
RUN scripts/install-sdk.sh  
  
# Declare volume for workspace storage  
RUN mkdir /workspace  
WORKDIR /workspace  
VOLUME ["/workspace"]  
  
# WebUI  
EXPOSE 80  
# Debug Port  
EXPOSE 15454  
# Node listen port  
EXPOSE 3000  
# Declare environnement variables  
ENV C9USER=user  
ENV C9PWD=password  
  
# Start container services  
CMD /usr/local/bin/node /c9sdk/server.js --port 80 -w /workspace --listen
0.0.0.0 --auth $C9USER:$C9PWD

