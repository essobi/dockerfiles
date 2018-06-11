FROM arm32v7/openjdk AS build  
  
COPY /hooks/qemu-arm-static /usr/bin/qemu-arm-static  
  
RUN apt-get update && apt-get install -y \  
gcc \  
make \  
sudo  
  
COPY wiringPi /wiringPi  
  
WORKDIR /wiringPi  
  
RUN ./build  
  
FROM arm32v7/openjdk  
  
COPY \--from=build /usr/local/lib/libwiring* /usr/local/lib/  
COPY \--from=build /usr/local/include/wiring* /usr/local/include/  
COPY \--from=build /usr/lib/libwiring* /usr/lib/  

