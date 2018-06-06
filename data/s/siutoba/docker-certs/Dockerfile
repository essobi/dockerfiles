FROM ubuntu  
MAINTAINER rdalinger@siu.edu.ar  
  
RUN apt-get update && apt-get install -y openssl \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
#Define una variable para poder usar mc y un par de directorios basicos  
RUN echo "export TERM=xterm" >> /root/.bashrc  
  
RUN mkdir /entrypoint.d \  
&& mkdir -p /CAs/configs  
  
COPY entrypoint.sh /  
COPY bin /bin  
COPY ./scripts/* /entrypoint.d/  
COPY ./configs/* /CAs/configs/  
  
ENV dir_rootCA=/CAs/rootCA  
ENV dir_interCA=/CAs/intermediate  
ENV dir_configCA=/CAs/configs  
ENV DOCKER_CONFIG_PATH=/CAs/rootCA  
  
ENV CA_KEY_LENGTH=4096  
ENV CA_DAYS=7300  
RUN chmod +x /entrypoint.sh \  
&& chmod +x /entrypoint.d/*.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
  

