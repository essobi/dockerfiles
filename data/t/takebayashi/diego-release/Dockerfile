FROM buildpack-deps:latest  
MAINTAINER Shun Takebayashi <shun@takebayashi.asia>  
  
RUN mkdir -p /root  
WORKDIR /root  
  
RUN apt-get update && apt-get install ruby ruby-dev -y  
  
RUN wget https://storage.googleapis.com/golang/go1.4.linux-amd64.tar.gz \  
&& tar xzf go1.4.linux-amd64.tar.gz \  
&& mv go / \  
&& rm go1.4.linux-amd64.tar.gz  
ENV PATH /go/bin:$PATH  
  
RUN mkdir -p workspace && cd workspace && git clone
https://github.com/cloudfoundry-incubator/diego-release.git  
WORKDIR /root/workspace/diego-release  
ENV GOPATH /root/workspace/diego-release  
ENV PATH /root/workspace/diego-release/bin:$PATH  
RUN git checkout develop && ./scripts/update  
  
RUN gem install --no-rdoc --no-ri bosh_cli  
RUN bosh create release --name diego  
  
CMD bash  

