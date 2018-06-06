FROM java:openjdk-7-jre  
  
MAINTAINER CloudSlang  
  
RUN groupadd -r cslang && useradd -r -g cslang cslang  
  
RUN mkdir -p /usr/cslang \  
&& cd /usr/cslang \  
&& wget "https://github.com/CloudSlang/cloud-
slang/releases/download/cloudslang-1.0.10/cslang-cli-with-content.tar.gzip" \  
&& tar xvf cslang-cli-with-content.tar.gzip \  
&& rm cslang-cli-with-content.tar.gzip  
  
WORKDIR /usr/cslang/cslang-cli/bin/  
  
ENTRYPOINT ["sh","cslang"]  

