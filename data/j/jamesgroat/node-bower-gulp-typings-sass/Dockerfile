FROM jamesgroat/node-bower-gulp-typings  
  
RUN apt-get update -y &&\  
apt-get install --no-install-recommends -y -q ruby &&\  
gem install sass &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/*  

