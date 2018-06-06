FROM phusion/baseimage:0.9.18  
  
MAINTAINER Luke Campbell <luke.campbell@rpsgroup.com>  
  
# General dependencies:  
RUN apt-get update && \  
apt-get install -y wget git build-essential && \  
rm -rf /var/lib/apt/lists/*  
# Install nodejs/npm and friends:  
RUN (curl -sL https://deb.nodesource.com/setup_6.x | bash) && \  
apt-get update && \  
apt-get install -y nodejs && \  
npm install -g grunt-cli && \  
rm -rf /var/lib/apt/lists/*  
# Install conda/python  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.0.5-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh && \  
export PATH="/opt/conda/bin:${PATH}" && \  
conda config --set always_yes yes --set changeps1 no && \  
conda config --set show_channel_urls True && \  
conda config --add create_default_packages pip && \  
conda update conda && \  
conda config --add channels conda-forge && \  
conda clean --all --yes  
ENV PATH=/opt/conda/bin:$PATH  
  
# Install container dependencies:  
# redis: Required for redis-cli ping in 50_configure  
# gunicorn: Required for webui  
RUN conda install redis=3.2.0 gunicorn=19.6.0 && \  
conda clean --all --yes  
  
# Add boot checks  
COPY contrib/docker/my_init.d/49_configure /etc/my_init.d/  
COPY contrib/docker/my_init.d/50_wait_for_services /etc/my_init.d/  
  
  
# Add our project  
RUN mkdir /usr/lib/ccweb /var/run/datasets /var/log/ccweb  
  
COPY cchecker_web /usr/lib/ccweb/cchecker_web  
COPY .bowerrc Gruntfile.js Assets.json bower.json package.json
requirements.txt\  
app.py setup.py worker.py /usr/lib/ccweb/  
COPY contrib/config/config.yml /usr/lib/ccweb/  
  
RUN useradd -m ccweb  
RUN chown -R ccweb:ccweb /usr/lib/ccweb /var/run/datasets /var/log/ccweb  
  
WORKDIR /usr/lib/ccweb  
# Install python dependencies  
# First, clean up requirements file to be compatible with conda pkgs  
RUN sed -i 's/redis==/redis-py==/' requirements.txt && \  
# Install what is possible using conda  
conda install --file requirements.txt && \  
conda clean --all --yes  
  
# Install extra plugins:  
RUN conda install cc-plugin-ncei && \  
conda install cc-plugin-glider && \  
conda clean --all --yes  
  
# Install local dependencies  
USER ccweb  
RUN npm install && \  
./node_modules/.bin/bower install && \  
grunt  
USER root  
  
# Add our daemons:  
RUN mkdir /etc/service/ccweb-app /etc/service/ccweb-worker-01  
COPY contrib/docker/runit/web.sh /etc/service/ccweb-app/run  
COPY contrib/docker/runit/worker.sh /etc/service/ccweb-worker-01/run  
RUN chmod +x /etc/service/ccweb-app/run /etc/service/ccweb-worker-01/run  
  
CMD ["/sbin/my_init"]  
EXPOSE 3000  

