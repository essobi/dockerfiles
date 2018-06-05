FROM debian:stretch  
  
RUN apt-get update && \  
apt-get install -y \  
debootstrap \  
e2fsprogs \  
kpartx \  
parted \  
python-setuptools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY setup.py /app/setup.py  
COPY bootstrapvz /app/bootstrapvz  
COPY bootstrap-vz /app/bootstrap-vz  
  
WORKDIR /app  
RUN ["python", "setup.py", "develop"]  
VOLUME /app/manifests  
  
ENTRYPOINT ["/app/bootstrap-vz"]  
  

