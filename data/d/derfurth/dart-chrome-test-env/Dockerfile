FROM markadams/chromium-xvfb  
  
RUN \  
apt-get -q update && apt-get install --no-install-recommends -y -q curl git
ca-certificates apt-transport-https openssh-client && \  
curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&
\  
curl
https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list
> /etc/apt/sources.list.d/dart_stable.list && \  
curl
https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_unstable.list
> /etc/apt/sources.list.d/dart_unstable.list && \  
apt-get update && \  
apt-get install dart && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
apt-get -q update && apt-get install -y -q \  
python python-pip unzip libgconf-2-4  
  
ENV DART_SDK /usr/lib/dart  
ENV PATH $DART_SDK/bin:$PATH  

