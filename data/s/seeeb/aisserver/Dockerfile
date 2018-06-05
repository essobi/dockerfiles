FROM java:7  
RUN apt-get update  
RUN apt-get install -y iputils-ping  
RUN apt-get install -y nano  
RUN mkdir -p /AISserver  
COPY . /AISserver  
WORKDIR /AISserver  
RUN javac *.java  
  

