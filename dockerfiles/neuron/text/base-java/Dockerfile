#
# Java Dockerfile
#
FROM neuron/base

# Install package
RUN apt-get update && \
    apt-get install -y \
    software-properties-common \
    openjdk-7-jdk \
    ant \
    ivy \
    curl \
    wget

#Cleanup
RUN apt-get clean
RUN rm -rf /tmp/*
