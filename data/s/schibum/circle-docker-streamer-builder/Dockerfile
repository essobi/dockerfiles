FROM buildpack-deps:xenial-scm  
  
RUN apt-get update  
RUN apt-get install -y libasound2-dev libbrlapi-dev libbz2-dev \  
libcairo2-dev libcap-dev libcups2-dev libcurl4-gnutls-dev libdrm-dev \  
libelf-dev libglib2.0-dev libglu1-mesa-dev libgnome-keyring-dev \  
libgtk2.0-dev libkrb5-dev libnspr4-dev libnss3-dev libpam0g-dev \  
libsctp-dev libspeechd-dev libsqlite3-dev libssl-dev libudev-dev \  
libwww-perl libxslt1-dev libxss-dev libxt-dev libxtst-dev \  
patch perl pkg-config python python-crypto python-psutil \  
python-yaml wdiff zip  
  
# RUN useradd -ms /bin/bash ubuntu  
# USER ubuntu  
# ENV HOME /home/ubuntu  
ENV HOME /root  
  
WORKDIR $HOME  
ENV PATH "${HOME}/depot_tools:${PATH}"  
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
\  
${HOME}/depot_tools  
  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true \  
\--bash-completion=true \--additional-components app alpha beta  
RUN google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true  
ENV PATH "${HOME}/google-cloud-sdk/bin:${PATH}"  
CMD gclient sync && ./build.sh  

