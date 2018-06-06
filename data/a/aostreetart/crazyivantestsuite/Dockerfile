################################################################  
  
# Dockerfile to build Crazy Ivan Test Container Images  
  
################################################################  
  
#Based on Ubuntu 14.04  
FROM ubuntu:14.04  
  
#Set the Maintainer  
MAINTAINER Alex Barry  
  
#Set up front end  
ENV DEBIAN_FRONTEND noninteractive  
  
#Ensure that base level build requirements are satisfied  
RUN apt-get update  
RUN apt-get install -y libprotobuf-dev protobuf-compiler git python python-dev
python-pip  
RUN apt-get clean  
RUN apt-get update  
  
#Get the DVS Interfaces  
RUN git clone https://github.com/AO-StreetArt/DvsInterface.git  
RUN cd DvsInterface && sudo make install  
  
#Pull the Protocol Buffer Tests  
RUN git clone https://github.com/AO-StreetArt/CrazyIvan_ProtoBufferTests.git  
  
# Compile the protocol buffer message  
RUN protoc -I=/usr/local/include/dvs_interface
--python_out=CrazyIvan_ProtoBufferTests/src/
/usr/local/include/dvs_interface/Scene.proto  
  
# Install Python Dependencies  
RUN pip install pyzmq protobuf  
  
# Entrypoint of the docker image  
ENTRYPOINT ["python", "CrazyIvan_ProtoBufferTests/SceneTest.py"]  

