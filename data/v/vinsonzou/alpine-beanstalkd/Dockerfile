FROM alpine:3.6  
MAINTAINER Vinson Zou <vinsoncou@gmail.com>  
  
ENV LIBS 'gcc git musl-dev make'  
RUN apk add --no-cache $LIBS  
  
COPY alpine.patch /alpine.patch  
  
WORKDIR /  
RUN git clone https://github.com/kr/beanstalkd  
RUN cd beanstalkd && patch -p0 < /alpine.patch && make && make install  
  
RUN rm -rf /alpine.patch /beanstalkd \  
&& apk del $LIBS\  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300"]  

