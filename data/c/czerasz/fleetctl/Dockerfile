FROM golang:1.6.0  
ARG FLEET_VERSION=v0.11.5  
RUN apt-get update && \  
apt-get install -y git ssh openssh-client && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp/fleet  
  
# Install fleet  
RUN git clone \--quiet -b $FLEET_VERSION \--single-branch
https://github.com/coreos/fleet.git ./ && \  
sh build && \  
mv ./bin/fleetctl /usr/bin/ && \  
rm -rf /tmp/fleet  
  
# Setup User to match Host User  
# Give the nre user superuser permissions  
ARG USER_ID=1000  
ARG GROUP_ID=1000  
ARG USER_NAME=fleet  
ARG GROUP_NAME=$USER_NAME  
RUN groupadd --gid $GROUP_ID $GROUP_NAME && \  
useradd --create-home --home /home/$USER_NAME \--uid ${USER_ID} \--gid
$GROUP_NAME \--groups sudo $USER_NAME && \  
echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
mkdir -p /home/$USER_NAME/.fleetctl && \  
chown $USER_NAME:$GROUP_NAME /home/$USER_NAME/.fleetctl  
  
COPY ./scripts/docker_entrypoint.sh /usr/bin/docker_entrypoint  
  
USER ${USER_NAME}  
WORKDIR /home/$USER_NAME  
ENTRYPOINT ["/usr/bin/docker_entrypoint"]  

