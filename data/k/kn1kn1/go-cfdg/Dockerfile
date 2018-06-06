FROM golang:1.8  
# install flex  
RUN apt-get update \  
&& apt-get -y --force-yes install flex bison libpng12-dev \  
&& rm -rf /var/cache/apt/archives/*.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
# make and install cfdg  
RUN mkdir -p /tmp/cfdg  
RUN curl -s
http://glyphic.s3.amazonaws.com/cfa/download/ContextFreeSource3.0.9.tgz \  
| tar --strip-components=1 -xz -C /tmp/cfdg \  
&& rm -rf ./ContextFreeSource3.0.9.tgz  
WORKDIR /tmp/cfdg  
RUN make \  
&& mkdir -p /app/usr/local/bin \  
&& cp cfdg /app/usr/local/bin \  
&& rm -rf /tmp/cfdg  
ENV PATH /app/usr/local/bin:$PATH  
  
RUN mkdir -p /app/.profile.d \  
&& echo "export PATH=\"/app/usr/local/bin:\$PATH\"" > /app/.profile.d/cfdg.sh
\  
&& echo "cd /app/user" >> /app/.profile.d/cfdg.sh  
  
# build go-cfdg  
WORKDIR /app/user  
COPY . /app/user  
RUN go build -o go-cfdg  
  
ENV PORT 3000  
#EXPOSE 3000  
CMD ./go-cfdg  

