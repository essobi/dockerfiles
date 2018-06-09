FROM kperson/ubuntu-java-7:latest  
  
MAINTAINER Kelton Person <https://github.com/kperson>  
  
#Server Code  
EXPOSE 8080  
WORKDIR /  
ADD . /code  
WORKDIR /code  
RUN ./build-sbt-repo.sh  
RUN sbt 'project hub' clean compile stage  
RUN mkdir /structure-data  
VOLUME /structure-data  
CMD ["hub/target/universal/stage/bin/hub", "--host", "0.0.0.0", "--port",
"8080"]  

