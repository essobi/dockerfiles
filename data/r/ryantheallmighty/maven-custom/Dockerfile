FROM maven:3-jdk-8  
MAINTAINER Ryan Dowling <ryan@ryandowling.me>  
  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y sudo
libc6:i386 libstdc++6:i386 && echo "ALL ALL=(ALL) NOPASSWD: ALL" >>
/etc/sudoers && rm -rf /var/lib/apt/lists/*  

