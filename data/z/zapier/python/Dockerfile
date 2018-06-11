FROM python:3.6.4-slim-stretch  
  
# Apt packages  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends \  
build-essential libpq-dev python-pip libffi-dev python3-dev git && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
apt-get purge -y && \  
git --version  
  
# Pipenv  
  
RUN pip install --upgrade pip pipenv==11.9.0  
# Workspace  
  
ENV PYTHONDONTWRITEBYTECODE true  

