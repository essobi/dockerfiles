FROM paulwoelfel/docker-gcloud  
  
RUN apt-get update && \  
apt-get -y install google-cloud-sdk-datastore-emulator && \  
pip install -U pip flake8 && \  
rm -rf /var/lib/apt/lists/*  

