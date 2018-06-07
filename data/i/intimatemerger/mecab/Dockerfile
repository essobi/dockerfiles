FROM python:2.7.12-alpine  
  
ADD mecab-0.996.tar.gz /tmp  
WORKDIR /tmp/mecab-0.996  
RUN apk add --no-cache build-base && \  
./configure && \  
make && \  
make check && \  
make install  
  
ENV NEOLODG_VERSION=0.0.5  
RUN apk add --no-cache git bash curl file openssl sudo && \  
curl -o /tmp/mecab-ipadic-neologd-$NEOLODG_VERSION.tar.gz
"https://codeload.github.com/neologd/mecab-ipadic-
neologd/tar.gz/v$NEOLODG_VERSION" && \  
tar xvfz /tmp/mecab-ipadic-neologd-$NEOLODG_VERSION.tar.gz -C /tmp  
WORKDIR /tmp/mecab-ipadic-neologd-$NEOLODG_VERSION  
RUN yes "yes" | ./bin/install-mecab-ipadic-neologd -n && \  
sed -i -e 's/ipadic/mecab-ipadic-neologd/' /usr/local/etc/mecabrc && \  
apk del git bash curl file openssl sudo && \  
rm -rf /tmp/*  
  
WORKDIR /  
  
CMD ["mecab"]

