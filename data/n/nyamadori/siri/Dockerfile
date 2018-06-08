FROM ruby:2.4.1  
ENV APP_ROOT /usr/local/app  
  
RUN \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get update && \  
apt-get install -y \  
mysql-client \  
redis-tools \  
nodejs \  
\--no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
\  
# install gems  
gem install bundler && \  
\  
# install mecab  
curl -sSL --output mecab-0.996.tar.gz
"https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE"
&& \  
tar -zxf mecab-0.996.tar.gz && \  
cd mecab-0.996 && \  
./configure --with-charset=utf-8 \--enable-utf8-only && \  
make && make check && make install && \  
ldconfig && \  
\  
# install mecab-ipadic  
cd ~ && \  
curl -sSL --output mecab-ipadic-2.7.0-20070801.tar.gz
"https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM"
&& \  
tar -zxf mecab-ipadic-2.7.0-20070801.tar.gz && \  
cd mecab-ipadic-2.7.0-20070801 && \  
./configure --with-charset=utf-8 \--enable-utf8-only && \  
make && make install && \  
\  
# install mecab-ipadic-NEologd  
cd ~ && \  
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \  
cd mecab-ipadic-neologd && \  
./bin/install-mecab-ipadic-neologd -n -y  
  
WORKDIR $APP_ROOT  
  
COPY Gemfile $APP_ROOT  
COPY Gemfile.lock $APP_ROOT  
  
RUN \  
bundle install --jobs=4  
  
COPY . $APP_ROOT  
COPY ./docker/bin/boot-app /usr/local/bin  

