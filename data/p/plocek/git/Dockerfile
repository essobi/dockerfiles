FROM alpine  
MAINTAINER Sebastian Plocek <sebastian@plocek.at>  
  
RUN apk --no-cache add git bash openssh  
RUN mkdir /git-workdir \  
mkdir /root/.ssh  
  
VOLUME ["/root/.ssh"]  
VOLUME ["/git-workdir"]  
  
WORKDIR /git-workdir  
  
CMD ["git","--help"]

