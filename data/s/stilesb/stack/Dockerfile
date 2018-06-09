FROM debian:jessie-slim  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
575159689BEFB442  
RUN echo 'deb http://download.fpcomplete.com/debian jessie main' | \  
tee /etc/apt/sources.list.d/fpco.list  
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y curl stack
bzip2  
RUN useradd -ms /bin/bash robot  
RUN groupadd nixbld && usermod -a -G nixbld robot  
ENV HOME /home/robot  
RUN mkdir -p /nix $HOME/.nixpkgs /home/robot/code/.stack-work && \  
chown -R robot /nix $HOME/.nixpkgs /home/robot/code/.stack-work  
ENV USER robot  
USER robot  
WORKDIR /home/robot  
RUN curl https://nixos.org/nix/install | sh  
RUN . $HOME/.nix-profile/etc/profile.d/nix.sh && \  
nix-channel --add https://nixos.org/channels/nixpkgs-unstable && \  
nix-channel --update  
WORKDIR /home/robot/code  

