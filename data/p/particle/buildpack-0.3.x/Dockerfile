FROM particle/buildpack-arduino-preprocessor  
  
RUN apt-get -y install gcc-arm-none-eabi make isomd5sum  
  
COPY hooks /hooks  
ADD workspace /workspace  

