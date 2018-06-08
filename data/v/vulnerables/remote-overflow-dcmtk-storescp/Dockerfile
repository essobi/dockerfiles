FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
valgrind \  
gdb \  
cgdb \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY src /src  
RUN cd /src && \  
./configure && \  
make  
  
EXPOSE 3000  
COPY main.sh /  
ENTRYPOINT ["/main.sh"]  
CMD ["default"]  
  

