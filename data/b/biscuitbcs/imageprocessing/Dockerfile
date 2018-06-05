FROM golang:1.8.3  
RUN apt-get update \  
&& apt-get -y install --no-install-recommends \  
lsb-release \  
libcv-dev \  
libopencv-dev \  
libopencv-contrib-dev \  
libhighgui-dev \  
libopencv-photo-dev \  
libopencv-imgproc-dev \  
libopencv-stitching-dev \  
libopencv-superres-dev \  
libopencv-ts-dev \  
libopencv-videostab-dev \  
&& curl -s https://raw.githubusercontent.com/h2non/bimg/master/preinstall.sh |
bash -  
  
ENV PORT 8080  
# install glide  
RUN curl https://glide.sh/get | sh \  
&& go get -v github.com/codegangsta/gin  
  
RUN mkdir -p /go/src/godocker  
WORKDIR /go/src/godocker  
  
COPY . .  
  
RUN glide install \  
&& go-wrapper install  
  
EXPOSE 8080  
EXPOSE 3000  
CMD ["go-wrapper", "run"]

