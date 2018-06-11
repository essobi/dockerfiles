FROM jeckhart/docker-yodle-base  
MAINTAINER John Eckhart "jeckhart@yodle.com"  
ADD build /build/docker-yodle-java7  
  
RUN /build/docker-yodle-java7/java7.sh && /build/docker-yodle-base/cleanup.sh  

