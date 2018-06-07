FROM openjdk:8  
LABEL maintainer="jesperbagge@gmail.com"  
  
# Define environment variables  
ENV VERSION latest  
ENV EXECUTABLES /minecraft/executables  
ENV REPOSITORY /minecraft/repository  
  
# Create base folders  
RUN mkdir -p $EXECUTABLES $REPOSITORY  
  
# Copy the current directory contents into the container at /minecraft  
ADD scripts/* $EXECUTABLES/  
  
# Open ports to the container  
EXPOSE 25565  
EXPOSE 25566  
EXPOSE 8123  
# Mount volume  
VOLUME $REPOSITORY  
  
# Set workdir  
WORKDIR $EXECUTABLES  
  
# Download and build latest spigot. Clean up and start server  
CMD ./update-and-run.sh  
  

