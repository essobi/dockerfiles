FROM golang:1.5  
RUN curl -s -o - https://get.docker.com/builds/Linux/x86_64/docker-1.6.2 >
/usr/local/bin/docker && chmod +x /usr/local/bin/docker  
RUN apt-get update  
RUN apt-get install -y daemontools daemontools-run  
  
ADD . /usr/src/dockerizer  
WORKDIR /usr/src/dockerizer  
  
RUN make deps  
RUN make build  
  
RUN ln -s /usr/src/dockerizer/build/linux/dockerizer /usr/bin/  
RUN ln -s /usr/src/dockerizer/build/linux/dockerizer /detect  
RUN ln -s /usr/src/dockerizer/build/linux/dockerizer /build  
RUN ln -s /usr/src/dockerizer/build/linux/dockerizer /sources  
RUN ln -s /usr/src/dockerizer/build/linux/dockerizer /export  
RUN ln -s /usr/src/dockerizer/build/linux/dockerizer /cleanup  
  
RUN /usr/bin/dockerizer buildpack install  
  
CMD ["/usr/bin/dockerizer"]  
  

