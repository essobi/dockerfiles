# Cloud9 IDE (http://c9.io) Dockerfile  
# Based on a work at https://github.com/kdelfour/cloud9-docker  
# pull base image.  
FROM kdelfour/supervisor-docker  
MAINTAINER Bjoern Stierand <bjoern-docker@innovention.de>  
  
# install base packages  
RUN apt-get update && apt-get install -yq \  
build-essential \  
g++ \  
curl \  
libssl-dev \  
apache2-utils \  
git \  
libxml2-dev \  
sshfs \  
tmux \  
puppet \  
puppet-lint \  
python-dev \  
python-pip  
  
# install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  
  
# install Cloud9  
RUN git clone https://github.com/c9/core.git /cloud9  
WORKDIR /cloud9  
RUN scripts/install-sdk.sh  
  
# tweak standlone.js conf  
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js  
  
# install CodeIntel  
RUN mkdir /tmp/codeintel && \  
pip install --download /tmp/codeintel codeintel==0.9.3 && \  
cd /tmp/codeintel && \  
tar xf CodeIntel-0.9.3.tar.gz && \  
mv CodeIntel-0.9.3/SilverCity CodeIntel-0.9.3/silvercity && \  
tar czf CodeIntel-0.9.3.tar.gz CodeIntel-0.9.3 && \  
pip install -U --no-index --find-links=/tmp/codeintel codeintel && \  
rm -rf /tmp/codeintel  
  
# add supervisord conf  
ADD conf/cloud9.conf /etc/supervisor/conf.d/  
  
# add volumes  
RUN mkdir /workspace  
VOLUME /workspace  
  
# clean up when done  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# expose ports  
EXPOSE 80  
EXPOSE 3000  
# start supervisor  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

