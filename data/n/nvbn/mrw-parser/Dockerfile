FROM openjdk:8  
MAINTAINER Vladimir Iakovlev <nvbn.rm@gmail.com>  
  
RUN apt-get update -yqq  
RUN apt-get upgrade -yqq  
RUN apt-get install curl -yqq --no-install-recommends  
RUN curl -s
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/usr/local/bin/lein  
RUN chmod +x /usr/local/bin/lein  
  
RUN adduser --disabled-password --gecos "" mrw-parser  
WORKDIR /home/mrw-parser  
USER mrw-parser  
  
COPY . /home/mrw-parser/  
USER root  
RUN chown -R mrw-parser /home/mrw-parser/  
USER mrw-parser  
  
RUN lein uberjar  
  
CMD java -jar target/mrw-parser-*-standalone.jar  

