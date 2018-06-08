FROM ubuntu:16.04  
MAINTAINER "Josh Lospinoso" josh@lospi.net  
RUN apt-get update && apt-get upgrade -y && apt-get install wget build-
essential -y  
RUN wget http://pocoproject.org/releases/poco-1.7.5/poco-1.7.5-all.tar.gz &&
tar xzvf poco-1.7.5-all.tar.gz  
WORKDIR poco-1.7.5-all  
RUN apt-get install libssl-dev libiodbc2 iodbc libmysqld-dev -y  
RUN ./configure  
RUN make  
RUN make install  
WORKDIR /  

