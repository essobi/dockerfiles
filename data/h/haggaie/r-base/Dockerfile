FROM debian:stretch  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-
recommends install \  
r-base-core \  
r-cran-ggplot2  
  
WORKDIR /document  
ENTRYPOINT ["R"]  

