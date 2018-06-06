FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -y install sqlite3 libsqlite3-dev  
RUN mkdir /app  
WORKDIR /app  
ADD store.sqlite3 /app/store.sqlite3  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
CMD "bash"  
  

