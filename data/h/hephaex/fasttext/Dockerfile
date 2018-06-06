FROM hephaex/ubuntu  
MAINTAINER Mario Cho <hephaex@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
git \  
python-dev \  
unzip \  
python-numpy \  
python-scipy && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apk/*  
  
RUN git clone https://github.com/facebookresearch/fastText.git /tmp/fastText
&& \  
rm -rf /tmp/fastText/.git* && \  
mv /tmp/fastText/* /root && \  
cd /root && \  
make  
  
COPY example-train.sh /root/  
COPY train.sh /root/  
COPY data /data  
COPY result /result  
  
RUN chown -R root:root /data /result  
RUN chmod -R 700 /data /result  
  
WORKDIR /root  
  
CMD ["./fasttext", "--allow-root"]  

