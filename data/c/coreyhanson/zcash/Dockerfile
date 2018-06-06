FROM ubuntu:16.04  
LABEL maintainer "Corey Ryan Hanson"  
#Adds Zcash repository.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
wget \  
ca-certificates \  
apt-transport-https && \  
rm -rf /var/lib/apt/lists/* && \  
wget -qO \- https://apt.z.cash/zcash.asc | apt-key add \- && \  
echo "deb [arch=amd64] https://apt.z.cash/ jessie main" | tee
/etc/apt/sources.list.d/zcash.list  
  
#Installs Zcash  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
zcash \  
sudo && \  
rm -rf /var/lib/apt/lists/*  
  
#Creates unprivelaged user.  
COPY create-user.sh /  
RUN chmod +x create-user.sh  
ARG docker_root_pass=zonkey  
ARG docker_unprivileged_user=zcash  
ARG docker_unprivileged_pass=zebra  
RUN /create-user.sh && \  
rm /create-user.sh  
USER $docker_unprivileged_user  
WORKDIR /home/$docker_unprivileged_user  
  
COPY zcash.conf /home/$docker_unprivileged_user/.zcash/zcash.conf  

