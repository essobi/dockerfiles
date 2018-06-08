FROM java:latest  
  
RUN apt-get update && apt-get -y install ffmpeg  
RUN git clone https://github.com/gbecan/questions-pour-un-generateur.git  
WORKDIR questions-pour-un-generateur  
RUN ./activator stage  
  
ENTRYPOINT ["./target/universal/stage/bin/questions"]  
  
CMD ["-Dconfig.file=/var/www/qpug/application.prod.conf"]

