FROM debian:unstable  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install reprotest -y && rm -rf /var/lib/apt  
  
COPY patch/build.py /usr/lib/python3/dist-packages/reprotest/build.py  

