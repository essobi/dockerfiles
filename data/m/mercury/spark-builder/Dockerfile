# spark-builder  
FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
bash \  
git \  
openjdk-8-jdk \  
python \  
python-pip \  
python-setuptools \  
python3-pip \  
python3-setuptools \  
curl \  
r-base-dev \  
maven \  
libopenblas-base \  
libatlas3-base \  
libnetlib-java \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install python-gitlab  
  
RUN pip install j2cli  
  
RUN (curl -L "https://raw.githubusercontent.com/wtsi-hgi/tarbomb-
disposal/master/tbd" > /usr/bin/tbd) && chmod a+x /usr/bin/tbd  
  
RUN curl -L -o /usr/local/bin/mc https://dl.minio.io/client/mc/release/linux-
amd64/mc && \  
chmod a+x /usr/local/bin/mc  
  
# Set workdir and entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  

