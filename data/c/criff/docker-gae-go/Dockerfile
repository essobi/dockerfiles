FROM circleci/golang:1.8.0  
ENV APPENGINE_VERSION=1.9.58  
ENV HOME=/home/circleci  
ENV SDK=https://storage.googleapis.com/appengine-
sdks/featured/go_appengine_sdk_linux_amd64-${APPENGINE_VERSION}.zip \  
PACKAGES="unzip git nodejs python-pygments" \  
PATH=${HOME}/go_appengine:${PATH} \  
GOROOT=${HOME}/go  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN sudo apt-get update && sudo apt-get install -y gcc musl-dev git python
${PACKAGES} && \  
curl -fo /tmp/gae.zip ${SDK} && unzip -q /tmp/gae.zip -d /tmp/ && mv
/tmp/go_appengine ${HOME}/go_appengine && \  
sudo apt-get clean  
  
# Install Hugo  
ENV HUGO_VERSION 0.20.7  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit  
  
RUN mkdir -p ${HOME}/hugo cd ${HOME}/hugo && wget
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
\  
&& tar xzf ${HUGO_BINARY}.tar.gz \  
&& sudo mv hugo /usr/local/bin/hugo \  
&& rm ${HUGO_BINARY}.tar.gz  
  
# Install util  
RUN sudo npm install -g yarn  
#RUN goapp get github.com/jstemmer/go-junit-report  

