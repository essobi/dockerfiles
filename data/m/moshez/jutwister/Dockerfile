FROM ubuntu:16.04  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get install -y python-virtualenv python-dev python3-venv python3-dev
libssl-dev build-essential libffi-dev && \  
python3 -m venv /jupyter && \  
python -m virtualenv /ncolony  
  
RUN /jupyter/bin/pip install --upgrade pip wheel && \  
/jupyter/bin/pip install twisted treq klein==17.2.0 jupyter  
  
RUN /ncolony/bin/pip install --upgrade pip wheel && \  
/ncolony/bin/pip install ncolony  
  
RUN mkdir -p /var/run/ncolony/messages /var/run/ncolony/config /root/.jupyter  
  
COPY jupyter.json remotemath.json /var/run/ncolony/config/  
  
COPY slash_root_jupyter_notebook_config.py
/root/.jupyter/jupyter_notebook_config.py  
  
RUN python3 -m venv /remotemath  
  
COPY setup.py /mnt/remotemath/  
COPY src/ /mnt/remotemath/src/  
  
RUN /remotemath/bin/pip install /mnt/remotemath  
  
ENTRYPOINT ["/ncolony/bin/twist", "ncolony", "--messages",
"/var/run/ncolony/messages", "--config", "/var/run/ncolony/config"]  

