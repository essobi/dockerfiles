FROM debian:stretch-slim  
  
LABEL maintainer "Anthony Mastrean <anthony.mastrean@gmail.com>"  
  
ENV TERM xterm-256color  
  
RUN apt-get update \  
&& apt-get install --yes \  
curl \  
libncurses5 \  
tar \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd --create-home adom  
  
WORKDIR /home/adom  
USER adom  
  
RUN curl --silent
http://www.ancardia.com/download/adom_linux_debian_64_3.0.6.tar.gz \  
| tar --extract --gzip --strip-components 1  
  
ENTRYPOINT ["./adom"]  

