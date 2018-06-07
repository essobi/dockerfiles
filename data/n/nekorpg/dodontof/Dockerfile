FROM lkwg82/h2o-http2-server  
MAINTAINER dev.ukatama@gmail.com  
  
RUN apk add --update \  
ruby \  
ruby-irb \  
ruby-json \  
ruby-rdoc \  
spawn-fcgi \  
wget \  
zip  
  
RUN apk add \  
make \  
gcc \  
fcgi-dev \  
libc-dev \  
ruby-dev \  
ca-certificates  
  
RUN update-ca-certificates  
  
RUN apk add libc-dev fcgi-dev make  
RUN gem install fcgi  
RUN apk del \  
make \  
gcc \  
fcgi-dev \  
libc-dev \  
ruby-dev  
  
RUN rm -rf /var/cache/apk/*  
  
WORKDIR /usr/local/src  
RUN wget http://www.dodontof.com/DodontoF/DodontoF_Ver.1.48.31.zip -q -O
DodontoF.zip \  
&& unzip DodontoF.zip \  
&& rm DodontoF.zip \  
&& sh -c 'sed -i -e "1s|/usr/local/bin/ruby|`which ruby`|"
DodontoF_WebSet/public_html/DodontoF/*.rb' \  
&& chmod +x DodontoF_WebSet/public_html/DodontoF/*.rb  
  
ADD dodontof-fcgi.rb /usr/local/src/DodontoF_WebSet/public_html/DodontoF  
RUN chmod +x DodontoF_WebSet/public_html/DodontoF/dodontof-fcgi.rb  
  
WORKDIR /etc/h2o  
ADD h2o.conf /etc/h2o  
  
CMD spawn-fcgi \  
-s /var/run/dodontof.sock \  
-d /usr/local/src/DodontoF_WebSet/public_html/DodontoF \  
-f /usr/local/src/DodontoF_WebSet/public_html/DodontoF/dodontof-fcgi.rb \  
& h2o -c /etc/h2o/h2o.conf  

