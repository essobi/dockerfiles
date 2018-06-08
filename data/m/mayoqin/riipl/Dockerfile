# Build from the RIIPL library @ https://hub.docker.com/r/riipl/3d_qifp/  
FROM riipl/3d_qifp:stable  
  
LABEL maintainer "Daniel Blezek blezek.daniel@mayo.edu"  
  
# Install Go and build grunt  
RUN apt-get update  
RUN apt-get install -y git-core wget curl ca-certificates  
run wget --no-check-certificate --quiet
https://storage.googleapis.com/golang/go1.7.linux-amd64.tar.gz  
RUN tar -C /usr/local -xzf go1.7.linux-amd64.tar.gz  
ENV GOPATH=/root  
ENV PATH=/usr/local/go/bin:${PATH}  
RUN go get github.com/Mayo-QIN/grunt  
  
# Cleanup  
RUN rm -fr /usr/local/go  
RUN rm -f go1.7.linux-amd64.tar.gz  
  
WORKDIR /riipl  
RUN mkdir -p /riipl/grunt_work  
RUN cp /root/bin/grunt /bin/grunt  
COPY gruntfile.yml /riipl/gruntfile.yml  
COPY config.ini /riipl/config.ini  
  
# What do we run on startup?  
ENTRYPOINT ["/bin/grunt", "/riipl/gruntfile.yml"]  
# We expose port 9901 by default  
EXPOSE 9901:9901  

