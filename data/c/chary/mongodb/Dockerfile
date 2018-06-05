FROM ubuntu:latest  
RUN apt-get update -y  
RUN echo "Helloworld"  
#this is for test  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN apt-get install -y software-properties-common  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep
DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.2 multiverse" | tee
/etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt-get update && apt-get install -y mongodb-org  
RUN mkdir -p /data/db  
EXPOSE 27017  
ENTRYPOINT ["/usr/bin/mongod"]  

