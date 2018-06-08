FROM ubuntu:xenial  
  
LABEL maintainer="yasuyuky@idein.jp"  
  
RUN \  
apt-get update \  
&& apt-get install -y python3 python3-pip curl unzip python3-cairo git
fontconfig locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p ~/.fonts \  
&& cd "$(mktemp -d)" \  
&& curl -sSLO --tlsv1 https://noto-
website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \  
&& echo "73728ed28fd1f4b1ac91bf759cad5f6e8b95bde662cff88f9a26a376a613a4a9
NotoSansCJKjp-hinted.zip" - sha256sum -c --strict - \  
&& unzip -d /usr/local/share/fonts/notosansjp/ NotoSansCJKjp-hinted.zip \  
&& rm NotoSansCJKjp-hinted.zip  
RUN cd ~/.fonts \  
&& curl -sSLO --tlsv1
https://github.com/google/fonts/raw/master/ofl/stoke/Stoke-Regular.ttf \  
&& curl -sSLO --tlsv1
https://github.com/google/fonts/raw/master/ofl/muli/Muli-Regular.ttf \  
&& curl -sSLO --tlsv1
https://github.com/google/fonts/raw/master/ofl/muli/Muli-Light.ttf \  
&& curl -sSLO --tlsv1
https://github.com/google/fonts/raw/master/ofl/muli/Muli-SemiBold.ttf \  
&& curl -sSLO --tlsv1
https://github.com/google/fonts/raw/master/ofl/muli/Muli-Bold.ttf \  
&& fc-cache -f -v \  
&& locale-gen ja_JP.UTF-8  
RUN pip3 install pip google-api-python-client  
RUN mkdir /work  
WORKDIR /work  
ENV LANG ja_JP.UTF8  

