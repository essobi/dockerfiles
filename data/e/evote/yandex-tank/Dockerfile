FROM ubuntu:latest  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:yandex-load/main \  
&& apt-get update \  
&& apt-get install -y python openssl ca-certificates curl libfontconfig
phantom phantom-ssl \  
&& apt-get install -y build-essential libxml2-dev libxslt1-dev python-dev
zlib1g-dev libssl-dev \  
&& cd /tmp \  
&& curl -skL https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install yandextank yatank-online \  
&& apt-get remove -y build-essential libxml2-dev libxslt1-dev python-dev
zlib1g-dev libssl-dev software-properties-common \  
&& apt-get autoremove -y \  
&& rm -rf /tmp/*  
  
EXPOSE 80  
  
CMD ["yandex-tank", "-c", "/opt/tank/tank.ini", "/opt/tank/url.list.txt"]

