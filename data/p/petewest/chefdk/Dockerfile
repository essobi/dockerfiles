FROM ubuntu:14.04  
RUN apt update && apt install -y \  
curl  
  
RUN curl -L
https://packages.chef.io/stable/ubuntu/12.04/chefdk_0.14.25-1_amd64.deb -o
chefdk.deb && \  
dpkg -i chefdk.deb && \  
rm chefdk.deb && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/repo"]  
WORKDIR /repo  
  
CMD ["/bin/bash"]  
  

