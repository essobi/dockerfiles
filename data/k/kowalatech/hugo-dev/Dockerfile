FROM deis/go-dev  
  
RUN apt-get update  
  
# Ruby  
RUN apt-get install ruby ruby-dev ruby-bundler curl apt-utils -y  
RUN gem install sass --no-user-install  
RUN gem install mime-types:2.0 rake cucumber capybara selenium-webdriver rspec
browserstack-local parallel_tests  
RUN gem install toml-rb  
  
#Hugo - October 2017 build  
ENV HUGO_VERSION=0.30.2  
ADD
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
/tmp  
RUN tar -xf /tmp/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz -C /tmp \  
&& mkdir -p /usr/local/sbin \  
&& mv /tmp/hugo /usr/local/sbin/hugo \  
&& rm -rf /tmp/hugo_${HUGO_VERSION}_linux_amd64  
  
# Node.JS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get install nodejs -y  
  
# Typescript  
RUN npm install -g typescript  
  
# Fontcustom  
RUN apt-get install zlib1g-dev fontforge -y  
RUN git clone https://github.com/bramstein/sfnt2woff-zopfli.git sfnt2woff-
zopfli && cd sfnt2woff-zopfli && make && mv sfnt2woff-zopfli
/usr/local/bin/sfnt2woff  
RUN git clone \--recursive https://github.com/google/woff2.git && cd woff2 &&
make clean all && mv woff2_compress /usr/local/bin/ && mv woff2_decompress
/usr/local/bin/  
RUN gem install --no-document fontcustom  
  
# Set up the workspace  
RUN mkdir -p /kowala  
WORKDIR /kowala/kowala.tech  
ENV PATH=$PATH:/kowala/workspace/bin  

