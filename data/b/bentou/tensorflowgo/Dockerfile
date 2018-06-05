FROM bentou/ubuntuxenialbazel  
  
# Based on
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/docker  
# Based on https://github.com/docker-library/golang/tree/master/1.7  
# maintener info  
MAINTAINER Lukasz Pyrzyk <lukasz.pyrzyk@gmail.com>, Jakub Bentkowski
<bentkowski.jakub@gmail.com>  
  
# Download and build TensorFlow.  
RUN git clone https://github.com/tensorflow/tensorflow.git && \  
cd tensorflow && \  
git checkout r0.11  
WORKDIR /tensorflow  
  
RUN apt-get update && apt-get install -y swig  
  
RUN ./configure  
RUN bazel build -c opt //tensorflow:libtensorflow.so  
  
RUN cp bazel-bin/tensorflow/libtensorflow.so /usr/local/lib  
  
# Download and install go  
ENV GOLANG_VERSION 1.7.3  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
508028aac0654e993564b6e2014bf2d4a9751e3b286661b0b0040046cf18028e  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  
  
WORKDIR /tensorflow  
RUN echo $(git rev-parse HEAD)  

