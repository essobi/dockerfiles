FROM openjdk:8-jdk-slim  
  
MAINTAINER USU Software AG  
  
RUN \  
apt-get update && \  
apt-get install -y -qq --no-install-recommends wget unzip python openssh-
client python-openssl git-core jq curl vim && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
curl -s https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt >
/usr/local/bin/sbt && chmod 0755 /usr/local/bin/sbt && \  
sbt about -sbt-create -sbt-version 0.13.16 -212  
  
# Prepare the image.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install the Google Cloud SDK.  
ENV HOME /  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --additional-components kubectl
alpha beta  
  
RUN mkdir /.ssh  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
CMD ["/bin/bash"]  
  
ENV HOME /root  
WORKDIR /root  

