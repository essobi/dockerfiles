FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -yq git wget ruby ruby-dev build-
essential && \  
gem install --no-ri \--no-rdoc bundler && \  
git clone https://github.com/tripit/slate && \  
cd /slate/source && \  
wget
https://raw.githubusercontent.com/CheckoutCrypto/site/master/modules/CheckoutCrypto/docs/API_CALLS.md
&& \  
cp ./API_CALLS.md ./index.md && cd .. && bundle install  
  
EXPOSE 4567  
WORKDIR /slate  
CMD ["bundle", "exec", "middleman", "server"]  

