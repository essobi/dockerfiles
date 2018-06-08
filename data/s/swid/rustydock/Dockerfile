FROM ubuntu:14.04  
MAINTAINER Sumedha Widyadharma <sumedha@widyadharma.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV force_color_prompt yes  
  
# Until there are cargo and rustc packages/ppas this will use rustup.  
# Package setup  
RUN apt-get update && \  
apt-get install -y curl git vim build-essential && \  
apt-get purge -y nano && \  
(curl https://static.rust-lang.org/rustup.sh | sudo bash) && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set up user  
RUN adduser --disabled-password --gecos "" user &&\  
echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user_is_root && \  
echo "export USER='Docker User'" >> /home/user/.bashrc  
  
USER user  
WORKDIR /home/user  
  
CMD /bin/bash  

