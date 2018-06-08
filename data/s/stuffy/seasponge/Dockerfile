FROM node:latest  
MAINTAINER stuffy@std-lab.co.za  
  
RUN apt-get update && \  
apt-get -y install \  
git \  
ruby-dev \  
rubygems && \  
npm install -g bower && \  
npm install -g grunt-cli && \  
npm install -g yo && \  
npm install -g generator-angular && \  
gem install sass && \  
gem install compass && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN git clone https://github.com/mozilla/seasponge.git seasponge && \  
cd seasponge && \  
npm install && \  
bower --allow-root install  
  
WORKDIR /seasponge  
  
COPY entry_point.sh /seasponge/  
  
EXPOSE 9000  
CMD ["sh", "entry_point.sh"]  

