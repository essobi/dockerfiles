  
# ... build this image with ...  
# docker build --tag=pinver/dlang:2.068.latest  
  
FROM pinver/dlang:base.latest  
  
# ... first of all, always update the packages ...  
RUN apt-get -q update  
  
# ... download (following redirect) and expand the ldc compiler ...  
RUN curl --insecure -L https://github.com/ldc-
developers/ldc/releases/download/v0.17.0-beta1/ldc2-0.17.0-beta1-linux-x86_64.tar.xz
| tar xJ && \  
mkdir -p /cellar/ldc && \  
mv ldc2-0.17.0-beta1-linux-x86_64 /cellar/ldc/0.17.0  
ENV PATH $PATH:/cellar/ldc/0.17.0/bin  
  
# ... download and install dmd ...  
RUN mkdir -p /cellar/dmd && \  
curl -L http://downloads.dlang.org/releases/2.x/2.068.2/dmd.2.068.2.zip >
dmd.2.068.2.zip && \  
unzip dmd.2.068.2.zip && \  
rm dmd.2.068.2.zip && \  
mv dmd2 /cellar/dmd/2.068 && \  
cp /cellar/dmd/2.068/linux/bin64/dmd /cellar/dmd/2.068/linux/bin64/dmd-2.068  
ENV PATH $PATH:/cellar/dmd/2.068/linux/bin64  
  

