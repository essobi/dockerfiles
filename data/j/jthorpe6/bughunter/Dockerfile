FROM debian  
ENV LC_ALL C.UTF-8  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
sudo \  
git \  
tmux \  
curl \  
locales \  
python-pip \  
python-dev \  
python3-pip \  
python3-dev \  
python-pycurl \  
libcurl4-openssl-dev \  
libssl-dev  
RUN useradd -ms /bin/bash bughunter && \  
usermod -g sudo bughunter && \  
echo "PS1='\w \$ >>> \\[\\]'" >> /home/bughunter/.bashrc && \  
echo "alias pyhttpd='python -m SimpleHTTPServer'" >> /home/bughunter/.bashrc
&& \  
echo "alias pyftpd='python -m pyftpdlib'" >> /home/bughunter/.bashrc && \  
echo "bughunter ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
WORKDIR /home/bughunter  
USER bughunter  
RUN pip install \  
httplib2==0.10.3 \  
colorlog==2.10.0 \  
protobuf==3.2.0rc2 \  
google==1.9.3 \  
wfuzz \  
pyftpdlib \  
requests \  
Scrapy==1.1.0rc3 \  
pybloom==1.1 \  
beautifulsoup \  
twisted==16.6.0 \  
w3lib \  
six \  
cssselect \  
pyopenssl \  
cryptography \  
queuelib \  
dnspython \  
tornado \  
bs4 \  
mechanize \  
prettytable \  
progressbar \  
colorama \  
terminaltables \  
termcolor \  
coloredlogs \  
lxml  
RUN pip3 install \  
docopt \  
bs4 \  
boto3==1.4.8 \  
botocore==1.8.2 \  
certifi==2017.11.5 \  
certstream==1.8 \  
chardet==3.0.4 \  
docutils==0.14 \  
idna==2.6 \  
jmespath==0.9.3 \  
multidict==3.3.2 \  
pipdeptree==0.10.1 \  
pyaml==17.10.0 \  
python-dateutil==2.6.1 \  
PyYAML==3.12 \  
requests==2.18.4 \  
requests-file==1.4.2 \  
s3transfer==0.1.11 \  
six==1.11.0 \  
termcolor==1.1.0 \  
tldextract==2.2.0 \  
urllib3==1.22 \  
websocket-client==0.44.0  
RUN git clone https://github.com/maurosoria/dirsearch
/home/bughunter/dirsearch && \  
git clone https://github.com/fuzzdb-project/fuzzdb /home/bughunter/fuzzdb && \  
git clone https://github.com/aboul3la/Sublist3r /home/bughunter/Sublist3r && \  
git clone https://github.com/m4ll0k/Spaghetti /home/bughunter/Spaghetti && \  
git clone https://github.com/DanMcInerney/xsscrapy /home/bughunter/xsscrapy &&
\  
git clone https://github.com/ekultek/pybelt /home/bughunter/pybelt && \  
git clone https://github.com/eth0izzle/bucket-stream /home/bughunter/bucket-
stream && \  
git clone https://github.com/AzizDammak/DorkScan /home/bughunter/DorkScan && \  
git clone https://github.com/ropnop/xxetimes /home/bughunter/xxetimes && \  
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
/home/bughunter/sqlmap-dev  
  

