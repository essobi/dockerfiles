############################################################  
# Dockerfile to build Pulsar container images  
# Based on ubuntu 16.04  
#############################################################  
  
# Set the base image to official ubuntu 16.04  
FROM ubuntu:16.04  
  
# File Author / Maintainer  
MAINTAINER Rafa Hernandez <https://github.com/fikipollo>  
  
################## BEGIN INSTALLATION ######################  
  
RUN apt-get update \  
&& apt-get install -y apt-utils vim python-dev python-pip curl wget
libcurl4-gnutls-dev unzip rsync libz-dev libssl-dev  
  
RUN pip install --upgrade pip \  
&& pip install virtualenv  
  
RUN mkdir /usr/local/pulsar_dist \  
&& cd /usr/local/pulsar_dist  
  
RUN wget -O /tmp/pulsar.zip
https://github.com/galaxyproject/pulsar/archive/master.zip  
RUN unzip /tmp/pulsar.zip -d /tmp/pulsar \  
&& mv /tmp/pulsar/*/* /usr/local/pulsar_dist/ \  
&& rm -r /tmp/pulsar/ \  
&& rm /tmp/pulsar.zip  
  
RUN cd /usr/local/pulsar_dist \  
&& virtualenv .venv \  
&& . .venv/bin/activate \  
&& pip install -r requirements.txt \  
&& cp app.yml.sample app.yml \  
&& mkdir dependencies \  
&& sed -i 's/#private_token:/private_token :/g' app.yml \  
&& sed -i 's/#
dependency_resolvers_config_file:/dependency_resolvers_config_file :/g'
app.yml \  
&& sed -i 's/host = localhost/host = 0.0.0.0/g' server.ini.sample \  
&& sed -i 's/PULSAR_CONFIG_DIR:-"."/PULSAR_CONFIG_DIR:-$PROJECT_DIRECTORY/g'
scripts/pulsar  
  
RUN wget -O /tmp/galaxy.zip
https://github.com/galaxyproject/galaxy/archive/master.zip  
  
RUN unzip /tmp/galaxy.zip -d /tmp/galaxy \  
&& mv /tmp/galaxy/* /usr/local/pulsar_dist/galaxy \  
&& rm -r /tmp/galaxy/ \  
&& rm /tmp/galaxy.zip  
  
RUN cd /usr/local/pulsar_dist \  
&& . .venv/bin/activate \  
&& sed -i 's/pysam==0.8.4+gx5/pysam==0.8.4/g'
/usr/local/pulsar_dist/galaxy/lib/galaxy/dependencies/pinned-requirements.txt
\  
&& pip install -r
/usr/local/pulsar_dist/galaxy/lib/galaxy/dependencies/pinned-requirements.txt  
  
COPY configs/entrypoint.sh /usr/bin/entrypoint.sh  
COPY configs/dependency_resolvers_conf.xml
/usr/local/pulsar_dist/dependency_resolvers_conf.xml  
COPY configs/app.yml /usr/local/pulsar_dist/app.yml  
COPY configs/local_env.sh /usr/local/pulsar_dist/local_env.sh  
  
RUN chmod +x /usr/bin/entrypoint.sh  
  
##################### INSTALLATION END #####################  
  
VOLUME ["/usr/local/pulsar"]  
  
EXPOSE 8913  
  
WORKDIR /usr/local/pulsar  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

