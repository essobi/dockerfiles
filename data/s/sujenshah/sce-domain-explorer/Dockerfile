  
# Pull base image.  
FROM ubuntu  
RUN echo "Hello world"  
WORKDIR /projects  
RUN apt-get update && \  
apt-get install -y software-properties-common wget git  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-add-repository universe && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN apt-get update && apt-get install -y git maven  
  
RUN git clone https://github.com/memex-explorer/sce-domain-discovery.git
/projects/domain-discovery && \  
cd /projects/domain-discovery && git pull --all && git checkout memex-dd  
  
RUN apt-get install -y python && \  
apt-get install -y python-setuptools python-dev build-essential && \  
easy_install pip  
  
WORKDIR /projects/domain-discovery/webui  
RUN pip install -r requirements.txt  
  
# Set up CDR dumper for MEMEX Domain Discovery  
WORKDIR /projects  
RUN git clone https://github.com/memex-explorer/sce.git && pip install pysolr  
  
RUN apt-get install -y nodejs-legacy && apt-get install -y npm && npm install
elasticdump -g  
RUN pip install --upgrade awscli  
  
WORKDIR /projects/domain-discovery/webui  
CMD ["python", "run.py"]  
  

