# Racket Dockerfile for building git HEAD  
#  
# Version 0.1  
FROM ubuntu  
  
MAINTAINER Asumu Takikawa, asumu@racket-lang.org  
  
# Get required packages to build and use Racket  
RUN apt-get update  
RUN apt-get install -y git make gcc libcairo2 libpango1.0-0 libjpeg8  
  
# Clone Racket repo and build the base system  
RUN git clone https://github.com/plt/racket.git  
RUN mkdir racket/racket/src/build  
RUN cd racket/racket/src/build && ../configure --prefix=/usr && make && make
install  
  
# Set up the packages in the distribution  
RUN cd racket && make local-source-catalog RACKET=/usr/bin/racket  
RUN cd racket && /usr/bin/raco pkg install -j 1 --catalog build/local/catalog
--auto -i main-distribution  
  
ENTRYPOINT ["/usr/bin/racket"]  

