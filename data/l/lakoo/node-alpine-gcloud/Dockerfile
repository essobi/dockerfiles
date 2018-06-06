FROM node:8-alpine  
MAINTAINER William Chong <williamchong@lakoo.com>  
  
RUN mkdir -p /opt  
WORKDIR /opt  
  
RUN apk add --no-cache \  
bash \  
ca-certificates \  
curl \  
git \  
openssh-client \  
python \  
tar \  
gzip  
  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN wget http://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --path-update=true \--bash-completion=true
\--rc-path=/root/.bashrc --additional-components app kubectl  
  
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/opt/google-cloud-sdk/lib/googlecloudsdk/core/config.json  
  
RUN mkdir ${HOME}/.ssh  
ENV PATH /opt/google-cloud-sdk/bin:$PATH  
  
WORKDIR /root  
CMD bash  

