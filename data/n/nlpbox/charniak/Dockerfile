# we use ubuntu for building, as alpine's g++ is too new  
FROM ubuntu:16.04 as builder  
MAINTAINER Arne Neumann <nlpbox.programming@arne.cl>  
  
RUN apt-get update -y && \  
apt-get install -y git make g++ flex  
  
WORKDIR /opt  
RUN git clone https://github.com/BLLIP/bllip-parser  
  
# To make the Charniak parser build process fully reproducible, we will  
# build a specific commit (i.e. the most recent commit  
# available on 2018-04-06).  
WORKDIR /opt/bllip-parser  
RUN git checkout -b 2018-04-06 f83be9f1453a47d5e5b9f9694da8d0950778fb99 && \  
make && rm -rf python # can't run bllip's own python tests b/c of nltk issue  
  
# we can't use alpine, as the build produces dynamically linked executables  
FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y python-pip && \  
pip install pytest sh && \  
rm -rf /var/lib/apt/lists/*  
  
ADD test_charniak.py /opt/bllip-parser/  
  
COPY \--from=builder /opt/bllip-parser /opt/bllip-parser  
  
WORKDIR /opt/bllip-parser  
  
ENTRYPOINT ["./parse.sh"]  
CMD ["/opt/bllip-parser/sample-text/sample-data.txt"]  

