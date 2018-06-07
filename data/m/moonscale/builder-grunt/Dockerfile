FROM node:5  
RUN apt-get update && \  
DEBIAN_FRONTEND=non-interactive apt-get install ruby-full pkg-config gcc g++
libfreetype6-dev libglib2.0-dev libcairo2-dev libharfbuzz-dev flex bison -y &&
\  
apt-get clean  
  
RUN gem install sass  
  
RUN npm install -g bower \  
&& npm install -g grunt-cli  
  
RUN cd /tmp \  
&& git clone git://repo.or.cz/ttfautohint.git \  
&& cd ttfautohint \  
&& ./bootstrap \  
&& ./configure --with-qt=no --with-doc=no \  
&& make install \  
&& cd .. \  
&& rm -rf ttfautohint  
  
RUN echo "user0:x:1000:1000:User 0:/tmp:/bin/false" >> /etc/passwd && \  
echo "user1:x:1001:1001:User 1:/tmp:/bin/false" >> /etc/passwd && \  
echo "user2:x:1002:1002:User 2:/tmp:/bin/false" >> /etc/passwd && \  
echo "user3:x:1003:1003:User 3:/tmp:/bin/false" >> /etc/passwd && \  
echo "user4:x:1004:1004:User 4:/tmp:/bin/false" >> /etc/passwd  

