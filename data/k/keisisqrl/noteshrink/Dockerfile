FROM python:latest  
  
RUN apt-get update \  
&& apt-get install -y optipng pngquant pngcrush \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install noteshrink  
  
RUN curl -Lo ipfs.tgz https://dist.ipfs.io/go-ipfs/v0.4.10/go-
ipfs_v0.4.10_linux-amd64.tar.gz \  
&& tar -zxvf ipfs.tgz \  
&& mv go-ipfs/ipfs /usr/local/bin/ \  
&& rm -rf go-ipfs ipfs.tgz  
  
CMD bash  

