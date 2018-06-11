FROM microsoft/dotnet:sdk  
  
  
# Install zip which isn't part of the base image. Also, s3cmd requires python-
dateutil.  
RUN apt-get update -y \  
&& apt-get install -y zip python-dateutil  
  
# Install s3cmd from the github releases because the version on apt-get is too
old. It can't handle  
# buckets with dots in the name.  
RUN cd / \  
&& curl -L
https://github.com/s3tools/s3cmd/releases/download/v1.6.1/s3cmd-1.6.1.tar.gz |
tar -xz  
ENV PATH=$PATH:/s3cmd-1.6.1  

