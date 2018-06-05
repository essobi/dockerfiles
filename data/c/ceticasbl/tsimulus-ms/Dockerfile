# Repository contains Dockerfile of Java8.  
FROM java:8  
MAINTAINER Alexandre Nuttinck  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
# Enable the usage of sources over https  
RUN apt-get update -y && apt-get install -y apt-transport-https  
  
# Add keyserver for SBT  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
  
# Install SBT  
RUN apt-get update -y && apt-get install sbt -y  
  
# EXPOSE On port 8001  
EXPOSE 8001  
# Compile the project  
RUN sbt compile  
  
# Run the sbt microservice  
CMD ["sbt","run"]  

