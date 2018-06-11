FROM phusion/baseimage  
  
RUN apt-get update && apt-get install -y \  
git \  
make \  
gcc \  
automake \  
autoconf \  
python \  
curl \  
libtool \  
check \  
pkg-config \  
nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV dockerize_version=0.2.0  
RUN \  
mkdir -p /usr/local/bin/ &&\  
curl -SL
https://github.com/jwilder/dockerize/releases/download/v${dockerize_version}/dockerize-
linux-amd64-v${dockerize_version}.tar.gz \  
| tar xzC /usr/local/bin  
  
RUN mkdir /code && \  
cd /code && \  
git clone https://github.com/statsite/statsite.git &&\  
cd /code/statsite &&\  
./autogen.sh &&\  
./configure &&\  
make &&\  
mv ./statsite /bin/statsite &&\  
mv /code/statsite/sinks /bin/sinks &&\  
chmod +x /bin/sinks/* &&\  
rm -rf /code  
  
COPY conf /conf  
COPY bin/dual-sink /bin/sinks/dual-sink  
COPY bin/start /bin/start  
  
ENTRYPOINT ["/bin/start"]  

