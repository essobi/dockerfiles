FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y curl ghostscript zip g++ gcc gzip perl5 wget cmake  
RUN wget http://weblogo.berkeley.edu/release/weblogo.2.8.2.tar.gz && tar xzvf
weblogo.2.8.2.tar.gz  
ENV PATH /weblogo:$PATH  
  
RUN mkdir -p /root/home/bin && echo "#!/usr/bin/sh" > /root/home/bin/blat &&
chmod a+x /root/home/bin/blat  
ENV PATH /root/home/bin:$PATH  
  
ADD http://homer.salk.edu/homer/configureHomer.pl /root/home/configureHomer.pl  
RUN sudo perl /root/home/configureHomer.pl -install  
  

