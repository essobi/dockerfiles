FROM ubuntu  
MAINTAINER TitanSnow <sweeto@live.cn>  
RUN apt-get update  
RUN apt-get install -y nodejs g++ git  
RUN git clone \--depth=1 --single-branch
https://github.com/TitanSnow/trashoj.git trashoj  
EXPOSE 1213  
WORKDIR /trashoj  
ENTRYPOINT nodejs booter.js  

