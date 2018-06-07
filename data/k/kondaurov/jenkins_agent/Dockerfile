from ubuntu:16.04  
RUN apt-get update && \  
apt-get install default-jre -y  
  
RUN apt-get install curl -y  
  
RUN apt-get install git -y  
  
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*  
  
RUN sudo apt-get update && \  
apt-get install openssh-server -y  
  
RUN curl -L
https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz |
tar -xz -C /usr/local  
  
RUN ln -s /usr/local/docker/docker /usr/local/bin/docker  
  
RUN groupadd docker  
  
RUN useradd -m -u 1000 -g 1000 -G docker jenkins  
  
RUN echo "jenkins:jenkins" | chpasswd  
  
RUN mkdir /var/run/sshd  
  
EXPOSE 22  
RUN echo "jenkins ALL=(ALL) ALL" >> etc/sudoers  
  
CMD ["/usr/sbin/sshd", "-D"]

