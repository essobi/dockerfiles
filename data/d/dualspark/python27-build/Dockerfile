# Docker image for building python projects  
#  
# Includes python, python-dev and pip  
FROM dualspark/static-s3-www  
  
RUN \  
sudo apt-get update -y && \  
sudo apt-get install software-properties-common curl zlib1g-dev build-
essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3
libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties
libffi-dev -y && \  
sudo mkdir -p /usr/local/src  
  
RUN \  
sudo apt-get install python-dev python-pip -y  
  
ENV HOME /root  
  
WORKDIR /root  
  
CMD ["bash"]  

