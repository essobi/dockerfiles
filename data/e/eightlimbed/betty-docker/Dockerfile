FROM alpine:latest  
RUN apk update && apk upgrade && apk add --no-cache perl git bash  
RUN git clone https://github.com/holbertonschool/Betty.git  
WORKDIR /Betty  
RUN ./install.sh  
CMD bash  

