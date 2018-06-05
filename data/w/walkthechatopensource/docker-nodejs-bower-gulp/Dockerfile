FROM library/node  
MAINTAINER Qiong Wu <qiong.wu@walkthechat.com>  
  
# Install Bower & Grunt  
RUN npm install -g bower gulp && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]

