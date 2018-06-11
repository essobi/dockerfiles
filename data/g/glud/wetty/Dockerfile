FROM node:0.10.38  
LABEL maintainer "Sebastian Tabares <sytabaresa@gmail.com>"  
  
WORKDIR /app  
RUN git clone https://github.com/krishnasrinivas/wetty .  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim nano asciinema  
#RUN useradd -d /home/glud -m -s /bin/bash glud  
#RUN echo 'glud:nomelase' | chpasswd  
EXPOSE 3000  
COPY ./docker_entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh", "node"]  
CMD ["app.js", "-p", "3000"]  

