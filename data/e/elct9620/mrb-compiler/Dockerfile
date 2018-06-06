FROM ruby:2.3-alpine  
  
ENV MRUBY_PATH /usr/src/mruby  
ENV MRUBY_VERSION 1.2.0  
RUN apk add --no-cache gcc g++ ruby make alpine-sdk bison abuild binutils git
bash  
RUN apk add --no-cache ca-certificates  
  
RUN mkdir -p $(dirname $MRUBY_PATH) && \  
git clone https://github.com/mruby/mruby.git $MRUBY_PATH && \  
cd $MRUBY_PATH && \  
git checkout $MRUBY_VERSION && \  
./minirake  
  
ADD compiler.sh /bin/mruby-compiler  
  
RUN chmod +x /bin/mruby-compiler  

