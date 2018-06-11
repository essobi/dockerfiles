FROM jeckhart/docker-yodle-base  
MAINTAINER John Eckhart "jeckhart@yodle.com"  
ADD build /build/docker-yodle-java8  
  
RUN /build/docker-yodle-java8/java8.sh && /build/docker-yodle-base/cleanup.sh  

