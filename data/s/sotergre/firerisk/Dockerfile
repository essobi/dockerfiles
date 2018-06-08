FROM ubuntu:14.04  
SHELL ["/bin/bash", "-c"]  
ENV HOME="/firecast"  
RUN apt-get update && apt-get install -y \  
gcc \  
curl \  
zip \  
bzip2 \  
git \  
clang \  
grads \  
awscli \  
ncftp \  
gdal-bin \  
java-common \  
ssmtp \  
make \  
default-jdk \  
wget \  
libxft2  
  
RUN git clone https://github.com/sotergre/FireRiskDev.git /firecast && \  
cd /firecast && \  
git checkout Expanded_Window  
  
WORKDIR /firecast  
ENV HOME="/firecast"  
RUN tar -xf DATA.tar.bz  
  
WORKDIR /firecast/lib  
RUN unzip HDFLOOK_LINUX_INTEL64 && \  
unzip gctpc && \  
unzip gscript && \  
cd /firecast/lib/gctpc/source && \  
make  
  
WORKDIR /firecast/SOURCE  
RUN ./MakeAll.sh && chmod 777 ../BIN/MOD7DownloaderHEMI.jar  
  
ARG awsdir  
ARG SECRET_ACCESS_KEY  
ARG ACCESS_KEY_ID  
  
#build command should include three --build-arg parameters  
# SECRET_ACCESS_KEY="Your key"  
# ACCESS_KEY_ID="Your ID"  
# awsdir="./.aws" **suggest copying your aws dir from ~/.aws to
FireRiskDev/.aws** in order to maintain small context  
#docker build --build-arg SECRET_ACCESS_KEY="" --build-arg ACCESS_KEY_ID=""
--build-arg awsdir="./.aws" -t <username>/repo:tag .  
ENV AWS_SECRET_ACCESS_KEY="$SECRET_ACCESS_KEY" \  
AWS_ACCESS_KEY_ID="$ACCESS_KEY_ID" \  
AWS_DEFAULT_PROFILE="default" \  
AWS_DEFAULT_REGION="us-east-1" \  
AWS_CONFIG_FILE="/firecast/.aws/config"  
COPY $awsdir/* /firecast/  
  
WORKDIR /firecast  
RUN mkdir /firecast/.aws && \  
echo "[default]" > /firecast/.aws/config && \  
echo "[default]" > /firecast/.aws/credentials && \  
echo 'aws_access_key_id = "$ACCESS_KEY_ID"' >> /firecast/.aws/credentials && \  
echo 'aws_secret_access_key = "$SECRET_ACCESS_KEY"' >>
/firecast/.aws/credentials && \  
echo 'output = table' >> /firecast/.aws/config && \  
echo 'region = us-east-1' >> /firecast/.aws/config && \  
aws configure list  
  
CMD ./firecast_init_manual_HEMI.sh  
  

