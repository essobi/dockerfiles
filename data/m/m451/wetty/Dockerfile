FROM node  
MAINTAINER Robert Szymczak <rszymczak@fum.de>  
  
ADD . /app  
WORKDIR /app  
RUN npm install  
RUN apt-get update  
RUN apt-get install -y vim  
  
# Create default user to run wetty in. This is necessary so we can connect to
a remote host  
RUN useradd -d /home/term -m -s /bin/bash term  
RUN echo 'term:term' | chpasswd  
USER term  
  
# Default ENV params used by wetty  
ENV REMOTE_SSH_SERVER 127.0.0.1  
ENV REMOTE_SSH_PORT 22  
ENV REMOTE_SSH_USER root  
  
# Expose our wetty port  
EXPOSE 3000  
# Set bash as default exec  
ENTRYPOINT ["/bin/bash"]  
  
# We default connecting to local host as root on port 22. When starting the
container you should provide the correct ENV e.g.:  
# docker run --name term -e REMOTE_SSH_SERVER=10.10.10.10 -e
REMOTE_SSH_PORT=22 -e REMOTE_SSH_USER=user -p 3000 -dt m451/wetty  
# exec connect script  
CMD ["connect.sh"]  

