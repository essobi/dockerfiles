FROM buildpack-deps:xenial-curl  
RUN apt update && apt install build-essential git zip libpng12-0 -y  
RUN wget https://dl.google.com/go/go1.10.1.linux-amd64.tar.gz && tar -C
/usr/local -xzf go1.10.1.linux-amd64.tar.gz  
RUN mkdir -p /go/src && mkdir -p /go/bin && mkdir -p /go/pkg  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install
-y nodejs  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install yarn -y  
  
ENV GOPATH=/go  
ENV PATH=$PATH:/usr/local/go/bin:/go/bin  

