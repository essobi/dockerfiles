FROM alpine  
MAINTAINER add ohmyadd@gmail.com  
COPY dist /root/dist  
  
# install dependencies  
RUN apk add --no-cache git python python-dev py-pip build-base libffi-dev
openssl-dev && \  
pip install --no-cache-dir -U pyOpenSSL requests && \  
  
# install wetftp from git  
git clone https://github.com/ohmyadd/wetftp /root/wetftp && \  
  
# configure wetftp  
cd /root/wetftp && cp wetftp.cfg.default wetftp.cfg && \  
mkdir data && \  
python /root/dist/generate_cert.py /root/wetftp/data && \  
mv /root/dist/entrypoint.py /usr/local/bin/ && \  
  
# clean up  
apk del git python-dev py-pip build-base libffi-dev && \  
rm -rf /var/cache/* && \  
rm -rf /root/dist/  
  
VOLUME /root/wetftp/log  
  
EXPOSE 20 21  
ENTRYPOINT ["entrypoint.py"]  

