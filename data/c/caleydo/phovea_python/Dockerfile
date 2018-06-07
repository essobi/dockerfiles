FROM python:2.7  
LABEL maintainer="samuel.gratzl@datavisyn.io"  
LABEL description="This is a base image for phovea server docker images"  
LABEL vendor="The Caleydo Team"  
LABEL version="1.1"  
  
COPY requirements*.txt docker_packages.txt ./  
RUN (!(test -s docker_packages.txt) || (apt-get update && (cat
docker_packages.txt | xargs apt-get install -y))) && pip install --no-cache-
dir -r requirements.txt

