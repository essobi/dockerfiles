FROM ubuntu:14.04  
COPY src /home/root/helloworld/src  
RUN apt-get update  
RUN apt-get -y install php5  
WORKDIR /home/root/helloworld  
ENTRYPOINT [ "php", "./src/HelloWorld.php" ]  

