FROM ubuntu  
  
RUN apt-get update && apt-get install -y build-essential uuid-dev iasl git
gcc-5 nasm python  
  
RUN mkdir -p /opt/src/ && \  
cd /opt/src && \  
git clone https://github.com/tianocore/edk2 && \  
cd edk2 && \  
make -C BaseTools  
  
ADD entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

