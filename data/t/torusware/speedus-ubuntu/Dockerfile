# Speedus-lite container  
From ubuntu:trusty  
MAINTAINER Jorge Docampo <jorge.docampo@torusware.com>  
  
ENV root_home /root  
  
RUN apt-get -qqy clean && apt-get -qqy update \  
&& apt-get -qqy upgrade \  
&& apt-get -qqy install wget unzip make gcc netbase \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV speedus_dir /opt/torusware/speedus  
ENV netpipe_dir $speedus_dir/benchmarks/NetPIPE-C  
  
WORKDIR /opt  
RUN mkdir torusware \  
&& cd torusware \  
&& wget http://dl.torusware.com/speedus/release/speedus-latest-linux.zip \  
&& unzip speedus-latest-linux.zip \  
&& rm speedus-latest-linux.zip \  
&& ln -s speedus-b* speedus \  
&& cp speedus/doc/README.image.txt $root_home/SPEEDUS_README.txt  
  
COPY speedus /usr/bin/speedus  
  
WORKDIR $netpipe_dir  
RUN make  
RUN cp NPtcp /usr/bin/NPtcp  
  
WORKDIR $root_home  

