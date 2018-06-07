# Docker image for building AWS images with Chef  
#  
# Currently installs: ChefDK 0.6.2 and Packer 0.8.0 along with  
# awscli 1.7.23  
FROM dualspark/static-s3-www  
  
RUN \  
sudo apt-get update -y && \  
sudo apt-get install -y unzip bundler  
  
ADD Gemfile /tmp/Gemfile  
  
RUN \  
wget -q https://s3-us-
west-2.amazonaws.com/packages.dualspark.com/static/chefdk/chefdk_0.6.2-1_amd64.ubuntu.deb
-O /tmp/chefdk.deb && \  
sudo dpkg --install /tmp/chefdk.deb && \  
sudo rm -f /tmp/chefdk.deb && \  
echo "PATH=/opt/chefdk/bin:$PATH" | tee -a ~/.profile && \  
cd /tmp && bundle install  
  
RUN \  
sudo mkdir -p /opt/packer && \  
wget -q https://s3-us-
west-2.amazonaws.com/packages.dualspark.com/static/packer/packer_0.8.0_linux_amd64.zip
-O /tmp/packer.zip && \  
sudo unzip /tmp/packer.zip -d /usr/bin && \  
sudo chmod +x /usr/bin/packer* && \  
sudo rm -f /tmp/packer.zip  
  
ENV HOME /root  
  
WORKDIR /root  
  
CMD ["bash"]  

