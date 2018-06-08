# Base docker image  
FROM debian:jessie  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN sed -i.bak 's/jessie main/jessie main contrib non-free/g'
/etc/apt/sources.list && \  
  
apt-get update && \  
apt-get install -y \  
wget  
  
RUN cd /root && \  
wget https://github.com/ginatrapani/todo.txt-
cli/releases/download/v2.10/todo.txt_cli-2.10.tar.gz && \  
tar -xvzf todo.txt_cli-2.10.tar.gz && \  
chmod +x todo.txt_cli-2.10/todo.sh  
  
ENTRYPOINT ["/root/todo.txt_cli-2.10/todo.sh"]  

