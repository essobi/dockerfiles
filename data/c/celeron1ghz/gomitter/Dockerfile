FROM celeron1ghz/perl:5.22  
MAINTAINER celeron1ghz <celeron1ghz@gmail.com>  
WORKDIR /root/gomitter  
  
RUN apk add \--update \--virtual=builder alpine-sdk wget git go \  
&& apk add \--update mariadb-dev \  
&& rm /usr/lib/libmysqld* \  
&& rm /usr/bin/mysql* \  
&& git clone https://github.com/celeron1ghz/Gomitter-Web.git ~/gomitter \  
&& /opt/perl-${PERL_MINOR_VERSION}/bin/perl
/opt/perl-${PERL_MINOR_VERSION}/bin/carton install \  
&& rm -Rf ~/.cpanm \  
&& GOPATH=/tmp go get github.com/mitchellh/cli \  
&& GOPATH=/tmp go get github.com/aws/aws-sdk-go \  
&& GOPATH=/tmp go get github.com/ryanuber/go-glob \  
&& GOPATH=/tmp go get github.com/golang/mock/gomock \  
&& GOPATH=/tmp go get github.com/mattn/go-shellwords \  
&& GOPATH=/tmp go get github.com/winebarrel/gcredstash || true \  
&& cd /tmp/src/github.com/winebarrel/gcredstash/ \  
&& GOPATH=/tmp:/tmp/src/github.com/winebarrel/gcredstash/ go build -a -tags
netgo -installsuffix netgo -o gcredstash \  
&& mv ./gcredstash /usr/bin/ \  
&& rm -Rf /tmp/src /tmp/pkg \  
&& apk del builder \  
&& find ~/gomitter/ -name *.tar.gz | xargs rm \  
&& find ~/gomitter/ -name *.pod | xargs rm  
  
EXPOSE 5353  
CMD ./script/gomitter_runner  

