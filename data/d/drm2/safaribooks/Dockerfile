FROM alpine:3.6  
MAINTAINER David R. Myers II <davidrmyersii@gmail.com>  
RUN apk update && \  
apk --no-cache add git ca-certificates openssl wget python python-dev musl-dev
libxml2-dev libxslt-dev openssl-dev libffi-dev gcc && \  
update-ca-certificates && \  
wget http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz -O
kindlegen.tar.gz && \  
mkdir ./kindlegen && \  
tar -xzf kindlegen.tar.gz -C ./kindlegen && \  
mv ./kindlegen/kindlegen /usr/bin/ && \  
rm -rf ./kindlegen && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install scrapy jinja2 beautifulsoup && \  
git clone https://github.com/ViciousPotato/safaribooks && \  
mkdir -p /safaribooks/output && \  
sed -i '/kindlegen/d' /safaribooks/crawl.sh && \  
echo 'cp *.epub books/' >> /safaribooks/crawl.sh && \  
echo 'sleep 1 && kindlegen *.epub' >> /safaribooks/crawl.sh && \  
echo 'cp *.mobi books/' >> /safaribooks/crawl.sh  
WORKDIR /safaribooks  
ENTRYPOINT ["./crawl.sh"]  

