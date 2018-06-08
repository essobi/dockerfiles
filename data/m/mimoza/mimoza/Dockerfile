# Docker image for Mimoza, the metabolic model generalizer  
#  
# The entrypoint runs Mimoza with command line arguments;  
# provide a volume for input data and results  
# cp $MODEL.xml $JOBDIR  
# docker run --volume $JOBDIR:/tmp mimoza:latest --model $MODEL.xml  
FROM ubuntu  
  
# Python3 needs an UTF-8 locale, http://bugs.python.org/issue19846  
ENV LANG C.UTF-8  
# Build-time environmental variable so that apt doesn't complain  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Create the development environment  
RUN apt update && \  
apt install -y git python3-setuptools python3-dev python3-pip python3  
RUN pip3 install --no-cache-dir --upgrade pip  
  
# Copy in the Mimoza source code then install  
COPY . /app  
WORKDIR /app  
RUN pip3 install --no-cache-dir .  
  
# Clean up the development environment to reduce image size  
RUN apt remove -y build-essential python3.5-dev && \  
apt autoremove -y  
  
# Mimoza jobs will be run in /tmp by a nonprivileged user  
RUN useradd mimoza  
USER mimoza  
WORKDIR /tmp  
  
# The entrypoint runs Mimoza with command line arguments  
ENTRYPOINT ["/usr/bin/python3", "/app/mimoza.py"]  

