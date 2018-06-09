FROM ubuntu:xenial  
  
ENV omnicore_version=omnicore-0.3.0  
LABEL omnicore_version="$omnicore_version" architecture="amd64"  
  
WORKDIR /data  
  
RUN apt-get update && apt-get -y install wget  
RUN wget
"https://bintray.com/artifact/download/omni/OmniBinaries/$omnicore_version-x86_64-linux-
gnu.tar.gz"  
RUN tar -xvzf "$omnicore_version-x86_64-linux-gnu.tar.gz" && rm
"$omnicore_version-x86_64-linux-gnu.tar.gz"  
RUN mv "$omnicore_version" omnicore && mkdir -p /root/.bitcoin/ && ln -sf
/data/usdt/bitcoin.conf /root/.bitcoin/bitc && echo "export
PATH=/data/omnicore/bin:$PATH" >> ~/.bashrc  
EXPOSE 18332 8332  
CMD ["/data/omnicore/bin/omnicored"]  

