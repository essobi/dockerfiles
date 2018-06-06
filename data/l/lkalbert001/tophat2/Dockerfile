FROM lkalbert001/ubuntu:14.04  
MAINTAINER lkalbert001  
  
COPY cufflinks-2.2.1.Linux_x86_64.tar.gz /opt  
  
WORKDIR /opt  
RUN set -xe \  
&& apt-get update\  
&& apt-get install -y bowtie2 samtools \  
&& tar -zxvf cufflinks-2.2.1.Linux_x86_64.tar.gz \  
&& find cufflinks-2.2.1.Linux_x86_64 -type f -executable |xargs -i mv {}
/usr/local/bin/ \  
&& wget
http://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.Linux_x86_64.tar.gz
\  
&& tar -zxvf tophat-2.1.1.Linux_x86_64.tar.gz \  
&& find tophat-2.1.1.Linux_x86_64/ -type f -executable| xargs -i mv {}
/usr/local/bin/ \  
&& rm -rf tophat-2.1.1.Linux_x86_64* cufflinks-2.2.1.Linux_x86_64* \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ['/bin/bash']  

