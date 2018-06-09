ARG CODE_VERSION=develop  
  
FROM continuumio/anaconda:latest  
  
# Install any needed packages specified and softwares  
RUN mkdir -p /model \  
&& apt-get update \  
&& apt-get install -y libzmq3 libzmq3-dev \  
&& conda install -y pyzmq  
  
# Set the working directory to /container  
WORKDIR /container  
  
# Copy containers/python/__init__.py and containers/python/rpc.py into
/container/  
COPY containers/python/__init__.py containers/python/rpc.py /container/  
  
# Define environment variable  
ENV CLIPPER_MODEL_PATH=/model

