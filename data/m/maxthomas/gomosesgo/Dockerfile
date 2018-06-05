FROM debian:latest  
  
RUN apt-get update -qq -y && apt-get install -y apt-utils debconf-utils  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get update -qq -y && apt-get install -y curl  
  
RUN mkdir app  
WORKDIR app  
  
RUN curl \  
-L https://github.com/maxthomas/gomosesgo/releases/download/v0.1.1-19-gd85bf7c-3-g929ecb9/gomosesgo_linux_amd64 \  
-o gomosesgo && chmod +x gomosesgo  
  
COPY bin bin/  
COPY build/scripts/run.sh .  
  
EXPOSE 8080  
ENTRYPOINT [ "./run.sh" ]  

