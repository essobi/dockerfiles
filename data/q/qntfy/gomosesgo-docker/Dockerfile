FROM debian:latest  
  
RUN apt-get update -qq -y && apt-get install -y apt-utils debconf-utils  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get update -qq -y && apt-get install -y curl git  
  
RUN mkdir app  
WORKDIR app  
RUN git clone https://github.com/qntfy/gomosesgo.git gmg --depth 1 && \  
mv gmg/bin . && \  
rm -rf gmg  
  
COPY gomosesgo .  
COPY image/run.sh .  
  
EXPOSE 8080  
ENTRYPOINT [ "./run.sh" ]  

