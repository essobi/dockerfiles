FROM debian:stretch  
MAINTAINER jonas@cowboyprogrammer.org  
  
RUN apt-get update -qq \  
&& apt-get install -qq -y \  
sudo \  
build-essential \  
ca-certificates \  
git \  
openjdk-8-jdk-headless \  
maven \  
devscripts \  
pandoc \  
debhelper \  
rpm \  
uuid-runtime \  
zip \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY userwrap.sh /bin/  
  
WORKDIR /workspace  
  
ENTRYPOINT ["/bin/userwrap.sh"]  

