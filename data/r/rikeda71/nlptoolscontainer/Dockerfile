FROM ubuntu:16.04  
  
WORKDIR work  
  
# lib & mecab  
RUN apt-get update && apt-get install -y \  
curl \  
make \  
gcc build-essential \  
libmecab2 libmecab-dev \  
mecab mecab-ipadic mecab-ipadic-utf8 mecab-utils \  
python python3 python-dev python3-dev python-mecab python-six \  
libboost-all-dev \  
language-pack-ja-base language-pack-ja \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# python  
RUN curl -L -o get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& python get-pip.py \  
&& python3 get-pip.py \  
&& rm -f get-pip.py \  
&& pip install mecab-python3 \  
&& pip install six  
  
# cabocha  
RUN curl -L -o CRF++-0.58.tar.gz
'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ'
\  
&& tar zxf CRF++-0.58.tar.gz \  
&& cd CRF++-0.58 \  
&& ./configure && make && make install && ldconfig \  
&& cd ../ \  
&& curl -c cabocha-0.69.tar.bz2 -s -L
'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU'
|grep confirm | sed -e "s/^.*confirm=\\(.*\\)&amp;id=.*$/\1/" | xargs -I{} \  
curl -b cabocha-0.69.tar.bz2 -L -o cabocha-0.69.tar.bz2
'https://drive.google.com/uc?confirm={}&export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU'
\  
&& tar xjf cabocha-0.69.tar.bz2 \  
&& cd cabocha-0.69 \  
&& ./configure --with-mecab-config='which mecab-config' \--with-charset=UTF8 \  
&& make && make install && ldconfig \  
&& cd python \  
&& python setup.py install \  
&& python3 setup.py install \  
&& cd ../../ \  
&& rm -rf CRF++-0.58* cabocha-0.69*  
  
# juman++  
RUN curl -L -o jumanpp-1.02.tar.xz 'http://lotus.kuee.kyoto-u.ac.jp/nl-
resource/jumanpp/jumanpp-1.02.tar.xz' \  
&& tar xJvf jumanpp-1.02.tar.xz \  
&& cd jumanpp-1.02\  
&& ./configure && make && make install \  
&& curl -L -o pyknp-0.3.tar.gz 'http://nlp.ist.i.kyoto-u.ac.jp/nl-
resource/knp/pyknp-0.3.tar.gz' \  
&& tar xvf pyknp-0.3.tar.gz \  
&& cd pyknp-0.3 \  
&& python setup.py install \  
&& python3 setup.py install \  
&& cd ../../ \  
&& rm -rf jumanpp-1.02*  
  
# other  
WORKDIR /home  
RUN cd ../ \  
&& rm -rf work  
ENV LANG=ja_JP.UTF-8  
ADD sample/ /home/  

