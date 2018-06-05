# Get the halo-scans component  
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.1.4 as downloader  
  
ARG HALO_SCANS_VERSION=v0.17  
RUN apt-get update && \  
apt-get install -y \  
git  
  
WORKDIR /app/  
  
RUN echo "Target branch for this build: $HALO_SCANS_VERSION"  
  
RUN git clone https://github.com/cloudpassage/halo-scans  
  
RUN cd halo-scans && \  
git archive --verbose --format=tar.gz -o /app/haloscans.tar.gz
$HALO_SCANS_VERSION  
  
##########################################################  
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.1.4  
MAINTAINER toolbox@cloudpassage.com  
  
ENV HALO_API_HOSTNAME=api.cloudpassage.com  
ENV HALO_API_PORT=443  
ENV DROP_DIRECTORY=/var/scans  
  
RUN apt-get update && apt-get install -y expect  
  
RUN mkdir /app  
COPY \--from=downloader /app/haloscans.tar.gz /src/haloscans.tar.gz  
COPY ./ /app/  
  
WORKDIR /src/  
  
RUN mkdir halo-scans && \  
cd halo-scans && \  
tar -zxvf ../haloscans.tar.gz  
  
WORKDIR /src/halo-scans  
RUN pip install .  
  
WORKDIR /app/tool/  
  
RUN pip install \  
boto3==1.5.6 \  
codeclimate-test-reporter==0.2.3 \  
coverage==4.2 \  
pytest==2.8.0 \  
pytest-cover==3.0.0 \  
pytest-flake8==0.1  
  
RUN py.test --cov=scanslib || py.test  
  
RUN mkdir -p $DROP_DIRECTORY  
  
CMD unbuffer python /app/tool/runner.py  

