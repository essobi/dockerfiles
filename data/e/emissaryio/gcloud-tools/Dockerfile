FROM emissaryio/python-virtualenv:1.0.2-3.6-slim  
  
RUN apt-get update && apt-get install -y \  
python2.7 \  
git  
  
ENV CLOUDSDK_PYTHON /usr/bin/python2.7  
WORKDIR /google  
ENV GOOGLE_DIR /google  
  
# gcloud  
RUN curl -s -o gcloud-sdk.tar.gz
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-168.0.0-linux-x86_64.tar.gz \  
&& tar xfz gcloud-sdk.tar.gz \  
&& rm gcloud-sdk.tar.gz  
  
# install deployment script dependencies  
RUN pip install --no-cache-dir \  
pyyaml  
  
# cloud_sql_proxy  
RUN curl -s -o cloud_sql_proxy
https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 \  
&& chmod +x cloud_sql_proxy \  
&& mkdir /cloudsql  
  
WORKDIR /  

