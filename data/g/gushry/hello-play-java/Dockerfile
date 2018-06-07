FROM gushry/play2  
MAINTAINER Gushiken  
  
ENV TARGET_DIR /opt  
  
WORKDIR ${TARGET_DIR}  
RUN activator new myapp hello-play-java  
  
WORKDIR ${TARGET_DIR}/myapp  
RUN ./activator clean compile stage  
  
EXPOSE 9000  
ENTRYPOINT ["./target/universal/stage/bin/myapp"]  

