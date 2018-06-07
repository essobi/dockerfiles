FROM google/golang  
  
RUN echo 'deb http://ftp.de.debian.org/debian wheezy-backports main' >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y liblz4-tool  
  
RUN go get github.com/fsouza/go-dockerclient  
RUN go get -v github.com/newrelic-forks/dogestry/dogestry  
  
CMD /home/ubuntu/go/dogestry  

