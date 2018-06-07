FROM ubuntu  
MAINTAINER David Zumbrunnen <zumbrunnen@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y install wget unzip python  
  
RUN wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip &&
unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --disable-installation-options  
RUN yes | google-cloud-sdk/bin/gcloud components update  
RUN mkdir /.ssh  
  
ENV PATH /google-cloud-sdk/bin:$PATH  
VOLUME ["/.config"]  
  
ADD gce-lb-presence /bin/gce-lb-presence  
  
CMD bash  

