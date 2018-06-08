FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y --no-install-recommends software-
properties-common  
  
RUN add-apt-repository ppa:fkrull/deadsnakes && \  
add-apt-repository ppa:openjdk-r/ppa  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
file \  
git \  
libffi-dev \  
libmysqlclient-dev \  
openjdk-8-jdk-headless \  
python3.5 \  
python3.5-dev \  
python3.5-venv \  
python-dev \  
python-pip \  
ruby ruby-dev \  
sudo && \  
rm -rf /var/cache/apt/archives  
  
RUN update-ca-certificates -f  
  
RUN gem install --no-ri --no-rdoc fpm  
  
RUN curl -L
"https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && chmod +x
/usr/local/bin/docker-compose  
  
RUN apt-get install -y python3-pip  
  
RUN python2 -m pip install --upgrade setuptools pip wheel && \  
python3 -m pip install --upgrade setuptools pip wheel  
  
# We install the linters script into directories that correspond to the  
# interpreter version so it is easy to fork the right one from pants.  
RUN pip2 install --install-option=--install-scripts=/opt/linters/python2/ pep8
flake8 autopep8 && \  
pip3 install --install-option=--install-scripts=/opt/linters/python3/ pep8
flake8 autopep8  
  
RUN pip2 install awscli  
  
# Spark 2.0.2  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.7.tgz
| tar -xz -C /opt/  
RUN ln -s spark-2.0.2-bin-hadoop2.7 /opt/spark-2.0.2  
  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz
| tar -xz -C /opt/  
RUN ln -s spark-2.1.1-bin-hadoop2.7 /opt/spark-2.1.1  
  
# Spark 2.3.0  
RUN curl -s https://archive.apache.org/dist/spark/spark-2.3.0/spark-2.3.0-bin-
hadoop2.7.tgz | tar -xz -C /opt/  
RUN ln -s spark-2.3.0-bin-hadoop2.7 /opt/spark-2.3.0  

