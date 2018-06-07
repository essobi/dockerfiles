FROM maven:3.5.2-jdk-8-slim  
LABEL maintainer "Yasumasa Suenaga <yasuenag@gmail.com>"  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y openjfx g++ ant binutils-dev libiberty-dev \  
libsnmp-dev make libtbb-dev  
ADD build.sh .  
  
ENTRYPOINT ["./build.sh"]  
  

