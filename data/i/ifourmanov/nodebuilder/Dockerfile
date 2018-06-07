FROM node:4.2.3  
MAINTAINER Ilya Fourmanov <ilya.fourmanov@gmail.com>  
COPY run.sh /root/run.sh  
RUN chmod +x /root/run.sh && useradd -u 3333 -d /home/builder -s /bin/bash -o
-m builder  
COPY npmrc /home/builder/.npmrc  
COPY bowerrc /home/builder/.bowerrc  
ENV EXTERNAL_ID 1000  
ENTRYPOINT [ "/root/run.sh" ]  

