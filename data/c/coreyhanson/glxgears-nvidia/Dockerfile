FROM nvidia/opengl:1.0-glvnd-runtime-ubuntu16.04  
LABEL maintainer "Corey Ryan Hanson"  
#Installs dependencies.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
sudo \  
glmark2 \  
mesa-utils && \  
rm -rf /var/lib/apt/lists/*  
  
#Creates unprivileged user.  
COPY /create-user.sh /  
RUN chmod +x create-user.sh  
ARG docker_root_pass=angela  
ARG docker_unprivileged_user=glxtest  
ARG docker_unprivileged_pass=george  
RUN /create-user.sh && \  
rm /create-user.sh  
USER $docker_unprivileged_user  
WORKDIR /home/$docker_unprivileged_user  

