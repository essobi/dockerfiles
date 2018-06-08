FROM golang:1.10.0  
MAINTAINER Yasushi kobayashi <kobayashi.yasushi@t-clue.com>  
  
ENV TZ=Asia/Tokyo  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN curl https://glide.sh/get | sh && \  
go get github.com/eure/kamimai/cmd/kamimai  

