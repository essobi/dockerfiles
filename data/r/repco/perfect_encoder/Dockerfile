###################  
# perfect_encoder #  
###################  
  
FROM repco/perfect_common:latest  
  
MAINTAINER colhom@gmail.com  
  
RUN apt-get -y install libtheora0 libvorbisenc2 libvorbis0a libvpx1  
  
RUN wget https://s3-us-west-1.amazonaws.com/perfect.assets/ffmpeg.tgz -O - |
tar zxvf - -C /usr  
  
RUN apt-get -y install gifsicle  
  
ADD . /root/gopath/src/github.com/repco/perfect_encoder  
RUN go get -v ./src/github.com/repco/perfect_encoder  
  
ENTRYPOINT ["/root/gopath/bin/perfect_encoder"]  
  
  

