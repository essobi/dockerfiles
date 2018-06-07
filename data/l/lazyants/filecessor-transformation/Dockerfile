FROM lazyants/docker-opencv-rust  
  
MAINTAINER Dmitriy Belyaev "dimabelyaev27@gmail.com"  
COPY ./project /tmp/app  
  
RUN cd /tmp/app && cargo build --release && mv target/release/transformer
/usr/bin && rm -rf /tmp/app  
  
ENV MEDIA_DIRECTORY="/media/"  
EXPOSE 3000  
VOLUME ["/media"]  
  
CMD ["transformer"]  

