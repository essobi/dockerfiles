FROM ruby:2.3.1-alpine  
  
MAINTAINER BlackGlory <woshenmedoubuzhidao@blackglory.me>  
  
COPY . /app  
WORKDIR /app  
  
RUN apk update && apk upgrade \  
&& apk add g++ \  
make \  
cmake \  
perl \  
icu-dev \  
py-pip \  
python \  
git \  
&& pip install docutils \  
&& gem install gollum \  
github-markdown \  
asciidoctor \  
creole \  
wikicloth \  
org-ruby \  
RedCloth \  
specific_install \  
&& gem specific_install https://github.com/BlackGlory/rugged_adapter.git \  
&& apk del g++ make cmake icu-dev py-pip \  
&& rm -rf /var/cache/apk/* /usr/local/bundle/cache /root/.gem/ /root/.gemrc
/root/.ash_history \  
&& find /usr/local/bundle/ \\( -name 'gem_make.out' -o -name 'mkmf.log' \\)
-delete \  
&& chmod +x /app/docker-entrypoint.sh  
  
VOLUME /wiki  
WORKDIR /wiki  
  
ENTRYPOINT ["/app/docker-entrypoint.sh", "gollum", "--adapter", "rugged"]  
  
EXPOSE 4567  

