FROM codenvy/ubuntu_jdk8  
  
RUN sudo apt-get update -y && \  
sudo apt-get \--no-install-recommends -y -q install git mercurial && \  
sudo mkdir /usr/local/go && wget -qO-
https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz | sudo tar xzf
- -C /usr/local/go \--strip-components=1  
ENV PATH /usr/local/go/bin:$PATH  

