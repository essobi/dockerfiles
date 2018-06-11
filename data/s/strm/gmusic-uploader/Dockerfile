FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
libav-tools \  
bpython3 \  
python3 \  
python3-pip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install gmusicapi-wrapper docopt-unicode  
  
COPY upload.py /  
  
VOLUME /data  
WORKDIR /data  
  
COPY main.sh /  
ENTRYPOINT ["/main.sh"]  
CMD ["default"]  
  

