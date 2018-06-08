FROM golang:1.10.1-stretch  
  
RUN apt-get update && apt-get install -y git nginx supervisor && \  
git clone \--branch v2.2 https://github.com/bitly/oauth2_proxy.git /go/src/app
&& \  
go get -d -v github.com/bitly/oauth2_proxy && \  
go install -v github.com/bitly/oauth2_proxy && \  
curl -s -L -o ./biscuit-linux_amd64.tgz
https://github.com/dcoker/biscuit/releases/download/v0.1.3/biscuit-
linux_amd64.tgz && \  
tar xzvf biscuit-linux_amd64.tgz && \  
mv biscuit /usr/bin/biscuit && \  
chmod +x /usr/bin/biscuit && \  
rm biscuit-linux_amd64.tgz && \  
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \  
python get-pip.py && \  
rm get-pip.py && \  
pip install awscli \--upgrade  
EXPOSE 4180  
  
COPY ./files/entrypoint.sh /entrypoint.sh  
COPY ./files/nginx.conf /etc/supervisor/conf.d/nginx.conf  
COPY ./files/oauth2_proxy.conf /etc/supervisor/conf.d/oauth2_proxy.conf  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["supervisord", "-n"]  

