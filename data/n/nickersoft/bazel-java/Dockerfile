FROM openjdk:8  
  
MAINTAINER nickersoft@gmail.com  
  
#################################  
# INSTALLING THE BASICS #  
#################################  
  
# Switch to the root user  
USER root  
  
# Update apt-get and install missing software  
RUN apt-get update  
RUN apt-get install -y git python python-dev maven curl pkg-config zip g++
zlib1g-dev unzip  
  
############################  
# INSTALLING BAZEL #  
############################  
  
# Download the install script  
RUN curl -L
https://github.com/bazelbuild/bazel/releases/download/0.14.0/bazel-0.14.0-installer-
linux-x86_64.sh > ./bazel-0.14.0-installer-linux-x86_64.sh  
RUN chmod +x bazel-0.14.0-installer-linux-x86_64.sh  
  
# Run the install script  
RUN ./bazel-0.14.0-installer-linux-x86_64.sh --user  
  
# Create a symlink in /usr/bin that points to /root/bazel  
RUN ln -sf /root/.bazel/bin/bazel /usr/bin/

