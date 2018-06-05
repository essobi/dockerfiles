FROM coreyhanson/lamp-base as unzip  
LABEL maintainer "Corey Ryan Hanson"  
  
#Downloads the repository script and makes executable.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
wget \  
unzip && \  
wget https://github.com/PoC-
Consortium/burstcoin/releases/download/1.3.6cg/burstcoin-1.3.6cg.zip && \  
mkdir burst-wallet && \  
cd burst-wallet && \  
unzip /burstcoin-1.3.6cg.zip && \  
mv burstcoin-1.3.6cg/* . && \  
rmdir burstcoin-1.3.6cg/ && \  
rm /burstcoin-1.3.6cg.zip && \  
chmod +x burst.sh  
  
#Begins stage 2 of image.  
FROM coreyhanson/lamp-base  
  
#Installs Burst Wallet dependencies.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
default-jre && \  
rm -rf /var/lib/apt/lists/*  
  
#Copies and enables setup scripts  
COPY burst-mariadb-config.sh /  
COPY create-user.sh /  
COPY modify-sudoers.sh /  
COPY start-burst-docker.sh /  
RUN chmod +x burst-mariadb-config.sh create-user.sh modify-sudoers.sh start-
burst-docker.sh  
  
#Creates unprivileged user and adds MariaDB privilages.  
ARG docker_root_pass=wizardhorse  
ARG docker_unprivileged_user=burst  
ARG docker_unprivileged_pass_arg=yannicorn  
ENV docker_unprivileged_pass=$docker_unprivileged_pass_arg  
RUN /create-user.sh && \  
/modify-sudoers.sh && \  
rm /create-user.sh modify-sudoers.sh  
  
#Configures MariaDB with database for Burst Wallet.  
RUN /burst-mariadb-config.sh && \  
rm /burst-mariadb-config.sh  
  
#Import burst repo from stage 1. Sets config file for accessing burst database
with a changeable password argument that mirrors that password for the
username.  
COPY \--from=unzip /burst-wallet /opt/burst-wallet  
COPY nxt.properties /opt/burst-wallet/conf/nxt.properties  
RUN sed -i "/nxt.dbPassword/ c\  
nxt.dbPassword=$docker_unprivileged_pass" \  
/opt/burst-wallet/conf/nxt.properties && \  
chown $docker_unprivileged_user /opt/burst-wallet/conf/nxt.properties  
  
#Switches to unprivelaged user.  
USER $docker_unprivileged_user  
WORKDIR /home/$docker_unprivileged_user  
  
CMD /start-burst-docker.sh  

