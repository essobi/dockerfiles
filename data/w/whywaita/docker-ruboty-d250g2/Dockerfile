FROM whywaita/mecab  
  
MAINTAINER whywaita <https://github.com/whywaita>  
  
RUN apt update -qq ;\  
apt install -y ruby ruby-dev zlib1g-dev ;\  
echo 'gem: --no-rdoc --no-ri' >> /.gemrc ;\  
gem install bundler ;\  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN mkdir -p /app/  
WORKDIR /app/  
ADD Gemfile Gemfile  
# ADD Gemfile.lock Gemfile.lock  
RUN bundle install --path=vendor/bundle  
  
ADD dic.csv dic.csv  
RUN /usr/local/libexec/mecab/mecab-dict-index -d
/usr/local/lib/mecab/dic/ipadic -u original.dic -f utf-8 -t utf-8 dic.csv  
RUN mv original.dic /usr/local/lib/mecab/dic/ipadic/  
RUN echo "userdic = /usr/local/lib/mecab/dic/ipadic/original.dic" >>
/usr/local/lib/mecab/dic/ipadic/dicrc  
  
RUN locale-gen ja_JP.UTF-8  
ENV LANG ja_JP.UTF-8  
ADD . /app/  
  
CMD bundle exec ruboty  

