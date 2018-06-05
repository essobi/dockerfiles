FROM ubuntu:15.10  
  
MAINTAINER Kezhu Wang kezhuw@gmail.com  
  
RUN apt-get update && \  
apt-get install -y wget && \  
wget
https://github.com/bazelbuild/bazel/releases/download/0.1.2/bazel_0.1.2-linux-x86_64.deb
&& \  
echo "9ba5326ed0561fe50cf04a8b4ee5940746f2760d29f64e7d67a99c9891c503a2
bazel_0.1.2-linux-x86_64.deb" | sha256sum --status --check - && \  
dpkg --install bazel_0.1.2-linux-x86_64.deb ; \  
rm bazel_0.1.2-linux-x86_64.deb && \  
apt-get install --fix-broken -y && \  
apt-get remove --auto-remove --purge -y wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

