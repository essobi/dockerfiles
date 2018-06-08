FROM circleci/golang:1.10.2  
ENV APPENGINE_VERSION=1.9.64  
ENV HOME=/home/circleci  
ENV SDK=https://storage.googleapis.com/appengine-
sdks/featured/go_appengine_sdk_linux_amd64-${APPENGINE_VERSION}.zip \  
PATH=${HOME}/go_appengine:${PATH}  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN sudo apt-get update && sudo apt-get install -y \  
musl-dev \  
nodejs \  
python-pygments \  
&& sudo apt-get clean \  
&& sudo rm -rf /var/lib/apt/lists/* \  
&& curl -fo /tmp/gae.zip ${SDK} \  
&& unzip -q /tmp/gae.zip -d /tmp/ \  
&& mv /tmp/go_appengine ${HOME}/go_appengine \  
&& rm /tmp/gae.zip  
  
# Install Hugo  
ENV HUGO_VERSION 0.30.2  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit  
  
RUN curl -sL -O
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
\  
&& tar xzf ${HUGO_BINARY}.tar.gz \  
&& sudo mv hugo /usr/local/bin/hugo \  
&& rm ${HUGO_BINARY}.tar.gz  
  
# Install util  
RUN sudo npm install -g yarn \  
&& go get -u gopkg.in/alecthomas/gometalinter.v2 \  
&& ln -s $GOPATH/bin/gometalinter.v2 $GOPATH/bin/gometalinter \  
&& gometalinter --install \  
&& curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
#RUN goapp get github.com/jstemmer/go-junit-report  

