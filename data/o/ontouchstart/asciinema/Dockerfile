FROM golang:1.7  
RUN apt-get -y upgrade  
RUN apt-get update -y  
RUN apt-get install -y locales vim git man  
RUN echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ADD github.com/asciinema/asciinema /go/src/github.com/asciinema/asciinema  
RUN go install github.com/asciinema/asciinema  
RUN asciinema --help  
WORKDIR /home  

