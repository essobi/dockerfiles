FROM xbox1994/sales-funnel:base  
  
RUN apt-add-repository -y ppa:rquillo/ansible  
RUN apt-get -y upgrade  
RUN apt-get update  
RUN apt-get install -y python-pip \  
groff-base \  
python-software-properties \  
software-properties-common \  
ntp \  
xvfb \  
ansible \  
git \  
bundler \  
nodejs \  
npm  
RUN pip install awscli  
  
# copy file  
WORKDIR /build  
RUN ln -s /usr/bin/nodejs /usr/bin/node && \  
echo "Europe/London" > /etc/timezon && \  
dpkg-reconfigure --frontend noninteractive tzdata && \  
npm config set strict-ssl false && \  
npm install phantomjs@2.1.1 -g

