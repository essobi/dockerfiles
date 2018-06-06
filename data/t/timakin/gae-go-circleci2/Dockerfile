FROM circleci/golang:1.9.0  
ENV GAE_GO_SDK_VERSION 1.9.24  
RUN sudo apt-get install -y netcat \  
python \  
python-pip \  
build-essential \  
libpng-dev  
  
RUN curl -o $HOME/go_appengine_${GAE_GO_SDK_VERSION}.zip
https://storage.googleapis.com/appengine-
sdks/featured/go_appengine_sdk_linux_amd64-${GAE_GO_SDK_VERSION}.zip  
RUN unzip -q -d $HOME $HOME/go_appengine_${GAE_GO_SDK_VERSION}.zip  
  
ENV PATH: $PATH:$HOME/go_appengine  
RUN go get -u github.com/golang/dep/cmd/dep  

