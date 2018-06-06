FROM ubuntu:latest  
MAINTAINER lovesb777@geninetworks.com  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
COPY ./key /home/ubuntu/key  
COPY ./script /home/ubuntu/script  
  
RUN sudo chmod 777 /home/ubuntu/script/init.sh  
  
WORKDIR /home/ubuntu  
  
CMD ["sh","/home/ubuntu/script/init.sh"]

