# Pull base image.  
FROM python:3.6  
MAINTAINER Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>  
  
# Install  
RUN apt-get update && apt-get install -y --no-install-recommends \  
zip \  
openssh-client \  
rsync \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install awscli  
  
# Define working directory.  
WORKDIR /workspace  
  
CMD ["/bin/bash"]  
ENTRYPOINT []

