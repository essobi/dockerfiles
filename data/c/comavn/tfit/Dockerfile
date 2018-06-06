FROM debian  
MAINTAINER Roel Harbers <roelharbers@gmail.com>  
# This Dockerfile builds and runs the tfit executable.  
# Usage:  
# docker build -t tfit  
# echo 'SGVsbG8sIFdvcmxkIQo=' | docker run -i --rm tfit  
ENV PACKAGES build-essential clang gengetopt git libc++-dev valgrind  
RUN apt-get update && apt-get install -qq -y --fix-missing --no-install-
recommends $PACKAGES  
  
ENV PROJECT_NAME tfit  
ENV PROJECT_PATH /$PROJECT_NAME  
RUN mkdir -p $PROJECT_PATH  
  
WORKDIR $PROJECT_PATH  
  
# Don't retrieve vendor code everytime our code changes  
COPY Makefile Makefile  
RUN make vendor  
  
COPY . .  
  
RUN make  
RUN make test  
  
CMD $PROJECT_PATH/build/tfit  

