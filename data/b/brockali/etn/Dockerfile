# Pull base image.  
FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y git libcurl4-openssl-dev build-
essential libjansson-dev autotools-dev automake  
RUN git clone https://github.com/wolf9466/cpuminer-multi && cd cpuminer-multi
&& ./autogen.sh && CFLAGS="-march=native" && ./configure && make  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define working directory.  
WORKDIR /  
  
COPY run.sh /  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  

