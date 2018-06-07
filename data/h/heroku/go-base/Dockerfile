FROM heroku/cedar:14  
RUN mkdir -p /app/user /app/.cache/go  
  
WORKDIR /app/user  
  
ENV GOVERSION go1.6.2  
ENV STACK cedar-14  
ENV HOME /app  
ENV GOROOT /app/.cache/go  
  
RUN curl -s --retry 3 -L
https://storage.googleapis.com/golang/$GOVERSION.linux-amd64.tar.gz | tar xz
-C /app/.cache  
RUN apt-get update && \  
apt-get -y install --no-install-recommends \  
mercurial bzr g++ gcc libc6-dev make libsasl2-dev && \  
apt-get -y clean && apt-get -y autoclean && rm -rf /var/lib/apt/lists/*  
ENV PATH $GOROOT/bin:$PATH  

