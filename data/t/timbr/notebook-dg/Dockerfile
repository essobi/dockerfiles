FROM ubuntu:xenial  
MAINTAINER Pramukta Kumar <pramukta.kumar@timbr.io>  
  
RUN apt update && \  
apt install -y git wget bzip2 build-essential libssl-dev libffi-dev  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64.deb && \  
dpkg -i dumb-init_*.deb  
  
WORKDIR /  
  
RUN wget --no-verbose http://repo.continuum.io/miniconda/Miniconda-latest-
Linux-x86_64.sh && \  
bash Miniconda-latest-Linux-x86_64.sh -p anaconda -b && \  
rm Miniconda-latest-Linux-x86_64.sh  
  
RUN /anaconda/bin/conda create -n default jupyter  
  
WORKDIR /juno-magic  
#ADD juno-magic.tar /juno-magic/  
RUN git clone -b development https://github.com/DigitalGlobe/juno-magic.git
/juno-magic  
RUN /anaconda/envs/default/bin/pip install .  
  
RUN /anaconda/envs/default/bin/jupyter nbextension install
https://raw.githubusercontent.com/minrk/ipython_extensions/master/nbextensions/gist.js  
  
RUN adduser --disabled-password --gecos "" gremlin --uid 2001  
RUN groupmod --gid 2001 gremlin  
  
ADD custom /anaconda/envs/default/lib/python2.7/site-
packages/notebook/static/custom  
RUN chown -R gremlin:gremlin /anaconda  
  
USER gremlin  
WORKDIR /home/gremlin  
EXPOSE 8888  
ADD custom anaconda/envs/default/lib/python2.7/site-
packages/notebook/static/custom  
  
ENV JUNO_KERNEL_URI=https://juno.timbr.io/juno/api/list  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--", "/anaconda/envs/default/bin/jupyter"]  
CMD ["notebook", "--port", "8888", "--no-browser", "-y", "--debug", "--ip",
"0.0.0.0", "--NotebookApp.base_url=/juno/notebook", "--
NotebookApp.allow_origin='*'", "--NotebookApp.token=''"]  
  

