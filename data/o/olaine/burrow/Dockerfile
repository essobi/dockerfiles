FROM golang:1.9.1  
MAINTAINER LinkedIn Burrow "https://github.com/linkedin/Burrow"  
RUN apt-get update && apt-get install -y curl bash git ca-certificates wget \  
&& update-ca-certificates \  
&& curl -sSO https://raw.githubusercontent.com/pote/gpm/v1.4.0/bin/gpm \  
&& chmod +x gpm \  
&& mv gpm /usr/local/bin  
  
ADD . $GOPATH/src/github.com/linkedin/Burrow  
RUN cd $GOPATH/src/github.com/linkedin/Burrow \  
&& gpm install \  
&& go install \  
&& mv $GOPATH/bin/Burrow $GOPATH/bin/burrow  
  
ADD docker-config /etc/burrow  
  
WORKDIR /var/tmp/burrow  
  
CMD ["/go/bin/burrow", "--config", "/etc/burrow/burrow.cfg"]  

