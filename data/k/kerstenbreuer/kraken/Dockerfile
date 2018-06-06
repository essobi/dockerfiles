FROM ubuntu:16.04  
LABEL author="Kersten Breuer, Zeller Team, EMBL 2017" \  
maintainer="kersten-breuer@outlook.com"  
  
# Install essential unix packages and dependencies:  
RUN apt-get update -y --fix-missing  
RUN apt-get install -y build-essential \  
wget \  
tar \  
make  
  
# Install Kraken:  
ENV KRAKEN_URL http://ccb.jhu.edu/software/kraken/dl/kraken-1.0.tgz  
RUN cd /usr/local/ \  
&& wget -O kraken.tgz ${KRAKEN_URL} \  
&& tar -xvzf kraken.tgz \  
&& rm kraken.tgz \  
&& mv kraken* kraken \  
&& cd kraken \  
&& bash install_kraken.sh .  
ENV PATH="/usr/local/kraken/:${PATH}"  
CMD ["kraken"]

