FROM philipz/rpi-raspbian  
  
ENV QEMU_EXECVE 1  
COPY . /usr/bin  
COPY HelloWorld.java /app/HelloWorld.java  
RUN [ "cross-build-start" ]  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jdk  
WORKDIR /app  
RUN javac HelloWorld.java  
RUN [ "cross-build-end" ]  

