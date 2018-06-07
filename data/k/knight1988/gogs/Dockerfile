FROM ubuntu:16.04  
# Install dependencies  
RUN apt-get update && apt-get install -y nano git sudo  
  
# Add git user  
RUN useradd -ms /bin/bash git && usermod -aG sudo git  
  
# Allow using sudo without password  
RUN echo 'git ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
# switch to user git  
USER git  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
RUN sudo chown -R git /app  
  
VOLUME ["/backup"]  
  
# Make port 22 3000 available to the world outside this container  
EXPOSE 22 3000  
# Run gogs when the container launches  
CMD ["/app/gogs/gogs", "web"]

