FROM ubuntu:17.10  
ENV CHECKM_VERSION=1.0.7  
RUN apt-get update && \  
apt-get install -y hmmer prodigal wget unzip python python-pip && \  
pip install checkm-genome==${CHECKM_VERSION} && \  
wget
"https://github.com/matsen/pplacer/releases/download/v1.1.alpha19/pplacer-
linux-v1.1.alpha19.zip" -O /root/pplacer.zip && \  
cd /root/ && \  
unzip pplacer.zip && \  
cp -r /root/pplacer-Linux-v1.1.alpha19/* /usr/local/bin/ && \  
rm -r /root/pplacer* && \  
echo "/var/spool/cwl/checkm_data_v1.0.7/" | checkm data setRoot
"/var/spool/cwl/checkm_data_v1.0.7/" && \  
apt-get purge -y wget unzip && \  
apt-get autoremove -y --purge && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

