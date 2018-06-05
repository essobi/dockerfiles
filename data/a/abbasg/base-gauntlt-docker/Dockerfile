FROM ubuntu:16.04  
ENV DIRB_WORDLISTS /opt/dirb/wordlists  
ENV SSLYZE_PATH /usr/local/bin/sslyze  
ENV PATH="/arachni/bin:${PATH}"  
# Install Dependencies  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
git \  
curl \  
libcurl3 \  
libcurl4-openssl-dev \  
wget \  
zlib1g-dev \  
libxml2-dev \  
libxslt1-dev \  
ruby \  
ruby-dev \  
ruby-bundler \  
chrpath libssl-dev libxft-dev \  
libfreetype6 libfreetype6-dev \  
libfontconfig1 libfontconfig1-dev \  
python python-dev python-pip python-software-properties \  
nmap \  
sqlmap && \  
rm -rf /var/lib/apt/lists/*  
  
# Install PhantomJs  
RUN mkdir /tmp/phantomjs \  
&& curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& cd /tmp/phantomjs \  
&& mv bin/phantomjs /usr/local/bin  
  
# Python Dependencies and sslyze  
RUN pip install --upgrade setuptools && \  
pip install wheel && \  
pip install sslyze && \  
pip install typing && \  
pip install requests && \  
pip install BeautifulSoup  
  
# Install dirb  
RUN \  
wget -q http://downloads.sourceforge.net/project/dirb/dirb/2.22/dirb222.tar.gz
&& \  
tar -C /opt -xzf dirb222.tar.gz && \  
rm -rf dirb222.tar.gz && \  
mv /opt/dirb222 /opt/dirb && \  
chmod -R +x /opt/dirb && \  
cd /opt/dirb && \  
bash ./configure && \  
make && \  
ln -s `pwd`/dirb /usr/local/bin/dirb  
  
# Install Arachni tools  
Run \  
wget -q
https://github.com/Arachni/arachni/releases/download/v1.5.1/arachni-1.5.1-0.5.12-linux-x86_64.tar.gz
&& \  
tar -xzf arachni-1.5.1-0.5.12-linux-x86_64.tar.gz && \  
rm -rf arachni-1.5.1-0.5.12-linux-x86_64.tar.gz && \  
mv arachni-* arachni  
  
# Install Garmr  
RUN \  
cd /opt && \  
git clone https://github.com/freddyb/Garmr.git && \  
cd Garmr && \  
python setup.py install  
  
# Install Gauntlt  
RUN gem install gauntlt --no-rdoc --no-ri  

