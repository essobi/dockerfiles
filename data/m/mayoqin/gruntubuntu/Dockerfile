  
# Build a UBUNTU based system  
FROM ubuntu:16.04  
MAINTAINER Paangiotis Korfiatis <Korfiatis.Panagiotis@mayo.edu>  
  
  
RUN apt-get update  
  
RUN apt-get install --no-install-recommends -y \  
ca-certificates \  
curl \  
mercurial \  
git-core  
  
RUN apt-get install -y build-essential  
RUN curl -s https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz|
tar -v -C /usr/local -xz  
  
ENV GOPATH /go  
ENV GOROOT /usr/local/go  
ENV PATH /usr/local/go/bin:/go/bin:/usr/local/bin:$PATH  
  
  
RUN go get github.com/Mayo-QIN/grunt  
  
# Install files  
RUN mkdir -p /grunt.d  
RUN cp /go/bin/grunt /bin/grunt  
COPY grunt.yml /gruntfile.yml  
  
# Start grunt in /data with the given gruntfile  
WORKDIR /data  
CMD ["/bin/grunt", "/gruntfile.yml"]  
  
# We expose port 9901 by default  
EXPOSE 9901:9901

