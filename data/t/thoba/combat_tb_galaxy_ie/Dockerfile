FROM ubuntu:14.04  
MAINTAINER Thoba Lose 'thoba@sanbi.ac.za'  
RUN groupadd -g 1047 galaxy \  
&& useradd -u 1097 galaxy -g galaxy  
  
RUN apt-get update  
  
RUN apt-get -y install software-properties-common \  
&& add-apt-repository ppa:webupd8team/java \  
&& apt-get -y update \  
&& apt-get -y install lsof net-tools supervisor nginx curl \  
# Install pip's dependency: setuptools:  
python python-dev python-distribute python-pip  
  
# Install miniconda to /miniconda  
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-
Linux-x86_64.sh  
RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b  
RUN rm Miniconda-latest-Linux-x86_64.sh  
ENV PATH=/miniconda/bin:${PATH}  
RUN conda update -y conda  
RUN conda install -y gunicorn click numpy pandas patsy python-dateutil PyYAML
scipy six statsmodels  
  
# Install Java  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections \  
&& apt-get -y install oracle-java7-installer \  
oracle-java7-set-default \  
&& rm -rf /var/lib/apt/lists/* \  
# Neo4j data and logs directories  
&& mkdir /data /logs  
  
# These environment variables are passed from Galaxy to the container  
# and help you enable connectivity to Galaxy from within the container.  
# This means your user can import/export data from/to Galaxy.  
ENV DEBIAN_FRONTEND=noninteractive \  
API_KEY=none \  
DEBUG=false \  
PROXY_PREFIX=none \  
GALAXY_URL=none \  
GALAXY_WEB_PORT=10000 \  
HISTORY_ID=none \  
REMOTE_HOST=none  
  
WORKDIR /opt  
  
# Install Neo4j  
ENV NEO4J_VERSION 2.3.3  
ENV NEO4J_EDITION community  
ENV NEO4J_DOWNLOAD_SHA256
01559c55055516a42ee2dd100137b6b55d63f02959a3c6c6db7a152e045828d9  
ENV NEO4J_DOWNLOAD_ROOT http://dist.neo4j.org  
ENV NEO4J_TARBALL neo4j-$NEO4J_EDITION-$NEO4J_VERSION-unix.tar.gz  
ENV NEO4J_URI $NEO4J_DOWNLOAD_ROOT/$NEO4J_TARBALL  
ENV NEO4J_AUTH none  
ENV NEO4J_REST_URL http://localhost:7474/db/data/  
  
RUN curl --fail --silent --show-error --location --output neo4j.tar.gz
$NEO4J_URI \  
&& echo "$NEO4J_DOWNLOAD_SHA256 neo4j.tar.gz" | sha256sum --check --quiet - \  
&& tar --extract --file neo4j.tar.gz --directory . \  
&& mv neo4j-* neo4j \  
&& rm neo4j.tar.gz  
  
ADD neo4j-server.properties /opt/neo4j/conf/neo4j-server.properties  
  
# VOLUMES  
VOLUME /data  
# Default Galaxy IE Volume  
VOLUME /import  
  
# ADD COMBAT-TB Web Code  
RUN wget https://bitbucket.org/sanbidev/combattb_web/get/v0.0.3.tar.gz &&
mkdir code && tar -C code --strip-components=1 -xf v0.0.3.tar.gz  
#ADD combattb_web /opt/code  
RUN pip install -r /opt/code/requirements.txt  
  
# Copy/Mount CTBReport data *For testing  
# ADD dataset_9999_files/jbrowse /data/jbrowse  
# ADD dataset_9999_files/neo4jdb /data/neo4jdb  
# RUN chown -R galaxy:galaxy /opt /data  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
# Nginx setup  
RUN rm /etc/nginx/sites-enabled/default  
ADD nginx.conf /etc/nginx/nginx.conf  
RUN nginx -t  
EXPOSE 80  
# RUN service supervisor restart  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

