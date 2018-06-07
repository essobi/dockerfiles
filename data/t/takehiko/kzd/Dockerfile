FROM alpine:latest  
LABEL maintainer Takehiko Murakawa <takehiko@sys.wakayama-u.ac.jp>  
  
RUN \  
apk --update add git openssh ruby imagemagick && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/* && \  
gem install --no-rdoc --no-ri test-unit rubyzip  
  
ENV LANG ja_JP.UTF-8  
WORKDIR /root  
  
RUN \  
git clone https://github.com/takehiko/kzd.git && \  
sed -e "s/..\\\/lib/kzd\\\/lib/" kzd/sample/hideyoshi.rb > hideyoshi.rb && \  
chmod +x hideyoshi.rb  
  
# docker build -t kzd .  
# docker run -it --rm kzd  
# docker run -it --rm -v $(pwd):/h kzd ./hideyoshi.rb /h  

