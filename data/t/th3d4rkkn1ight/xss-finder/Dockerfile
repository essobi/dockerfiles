FROM debian  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
git \  
wget \  
vim \  
locales \  
python-pip \  
python-dev \  
python3-pip \  
python3-dev \  
python-pycurl \  
curl \  
libssl-dev \  
libcurl4-openssl-dev  
RUN git clone https://github.com/DanMcInerney/xsscrapy /opt/xsscrapy && \  
git clone https://github.com/AzizDammak/DorkScan /opt/DorkScan && \  
wget https://raw.githubusercontent.com/tomsqr94/Useful-Files/master/.vimrc -P
/root/ && \  
wget https://raw.githubusercontent.com/tomsqr94/Docker/master/XSS-
Finder/customScanner.sh -P /opt/xsscrapy/  
RUN chmod +x /opt/xsscrapy/customScanner.sh && rm
/opt/xsscrapy/requirements.txt  
WORKDIR /opt/xsscrapy/  
RUN pip install \  
asn1crypto==0.24.0 \  
attrs==17.4.0 \  
backports-abc==0.5 \  
BeautifulSoup==3.2.1 \  
beautifulsoup4==4.6.0 \  
bitarray==0.8.1 \  
bs4==0.0.1 \  
certifi==2018.1.18 \  
cffi==1.11.4 \  
chardet==3.0.4 \  
colorama==0.3.9 \  
coloredlogs==9.0 \  
colorlog==2.10.0 \  
constantly==15.1.0 \  
cryptography==2.1.4 \  
cssselect==1.0.3 \  
dnspython==1.15.0 \  
enum34==1.1.6 \  
google==1.9.3 \  
html5lib==1.0.1 \  
httplib2==0.10.3 \  
humanfriendly==4.7 \  
idna==2.6 \  
incremental==17.5.0 \  
ipaddress==1.0.19 \  
keyring==10.1 \  
keyrings.alt==1.3 \  
lxml==4.1.1 \  
mechanize==0.3.6 \  
monotonic==1.4 \  
parsel==1.3.1 \  
prettytable==0.7.2 \  
progressbar==2.3 \  
protobuf==3.2.0rc2 \  
pyasn1==0.4.2 \  
pyasn1-modules==0.2.1 \  
pybloom==1.1 \  
pycparser==2.18 \  
pycrypto==2.6.1 \  
pycurl==7.43.0.1 \  
PyDispatcher==2.0.5 \  
pyftpdlib==1.5.3 \  
pygobject==3.22.0 \  
pyOpenSSL==17.5.0 \  
pyparsing==2.2.0 \  
pyxdg==0.25 \  
queuelib==1.4.2 \  
requests==2.18.4 \  
Scrapy==1.1.0rc3 \  
SecretStorage==2.3.1 \  
service-identity==17.0.0 \  
singledispatch==3.4.0.3 \  
six==1.11.0 \  
termcolor==1.1.0 \  
terminaltables==3.1.0 \  
tornado==4.5.3 \  
Twisted==16.6.0 \  
urllib3==1.22 \  
w3lib==1.18.0 \  
webencodings==0.5.1 \  
wfuzz==2.2.9 \  
zope.interface==4.4.3  
RUN pip3 install \  
beautifulsoup4==4.6.0 \  
boto3==1.4.8 \  
botocore==1.8.2 \  
bs4==0.0.1 \  
certifi==2017.11.5 \  
certstream==1.8 \  
chardet==3.0.4 \  
cryptography==1.7.1 \  
docopt==0.6.2 \  
docutils==0.14 \  
idna==2.6 \  
jmespath==0.9.3 \  
keyring==10.1 \  
keyrings.alt==1.3 \  
multidict==3.3.2 \  
pipdeptree==0.10.1 \  
pyaml==17.10.0 \  
pyasn1==0.1.9 \  
pycrypto==2.6.1 \  
pygobject==3.22.0 \  
python-dateutil==2.6.1 \  
pyxdg==0.25 \  
PyYAML==3.12 \  
requests==2.18.4 \  
requests-file==1.4.2 \  
s3transfer==0.1.11 \  
SecretStorage==2.3.1 \  
six==1.11.0 \  
termcolor==1.1.0 \  
tldextract==2.2.0 \  
urllib3==1.22 \  
websocket-client==0.44.0  
ENTRYPOINT ["/opt/xsscrapy/customScanner.sh"]  

