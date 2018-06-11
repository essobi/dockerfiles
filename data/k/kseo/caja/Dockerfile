FROM golang  
MAINTAINER Kwang Yul Seo <kwangyul.seo@gmail.com>  
  
ENV CAJA_PATH /go/src/github.com/kseo/caja/  
RUN curl https://glide.sh/get | sh  
  
WORKDIR $CAJA_PATH  
ADD glide.yaml glide.lock $CAJA_PATH  
RUN glide install  
  
ADD . $CAJA_PATH  
RUN go install -tags 'netcgo'  
  
ADD caja.yaml /go/bin  
WORKDIR /go/bin  
CMD ["caja"]  
  
EXPOSE 8080  

