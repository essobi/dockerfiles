FROM clojure:boot-alpine  
MAINTAINER Ignorabilis  
  
COPY . /opt/ignorabilis-src  
  
RUN mkdir /opt/ignorabilis \  
&& cd /opt/ignorabilis-src \  
&& boot ignorabilis-build \  
&& cp /opt/ignorabilis-src/target/project.jar /opt/ignorabilis/project.jar \  
&& rm -rf /opt/ignorabilis-src  
  
WORKDIR /opt/ignorabilis  
ENTRYPOINT []  
EXPOSE 80  
CMD java -jar project.jar  

