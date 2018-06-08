FROM ubuntu:16.10  
MAINTAINER Nuno Agostinho <nunodanielagostinho@gmail.com>  
  
RUN apt-get update  
  
# samtools  
# Usage: samtools [OPTIONS]  
RUN apt-get install -y gcc  
RUN apt-get install -y libncurses5-dev  
RUN apt-get install -y libbz2-dev  
RUN apt-get install -y liblzma-dev  
RUN apt-get install -y libcurl4-openssl-dev  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y zlib1g-dev  
RUN apt-get install -y make  
  
ENV SW=/root/software  
WORKDIR ${SW}  
  
ENV samtools=samtools-1.5  
ADD ${samtools}.tar.bz2 .  
WORKDIR ${samtools}  
  
RUN ./configure  
RUN make  
RUN make install  
WORKDIR ${SW}  
  
# MISO  
# Usage: miso [OPTIONS]  
# For instance, miso --run  
ADD get-pip.py .  
RUN apt-get install -y python  
RUN python get-pip.py  
RUN rm get-pip.py  
  
RUN pip install --upgrade pip  
RUN pip install numpy  
RUN pip install scipy  
RUN pip install pysam  
  
RUN apt-get install -y python-dev  
RUN apt-get install -y build-essential  
RUN pip install matplotlib  
  
RUN apt-get install -y bedtools  
RUN pip install misopy

