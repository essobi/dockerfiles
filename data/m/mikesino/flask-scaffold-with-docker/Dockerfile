FROM ubuntu:16.04  
LABEL version="1.0"  
LABEL maintainer="mike@mike-sino.eu.org"  
  
# updata ubuntu  
RUN apt-get update -y  
RUN apt-get install -y \  
git \  
curl \  
build-essential \  
supervisor \  
vim  
  
# Install Miniconda  
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh  
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b  
RUN rm Miniconda3-latest-Linux-x86_64.sh  
ENV PATH $PATH:/miniconda/bin  
RUN conda update -y conda  
RUN pip install --upgrade pip  
  
# Set supervisord.comf  
RUN touch /tmp/supervisor.sock  
RUN touch /tmp/supervisord.pid  
COPY init/tools_config/supervisord.conf /etc/supervisor/supervisord.conf  
  
# Start supervisor using systemd  
COPY init/systemd/supervisor.service /lib/systemd/system/supervisor.service  
RUN systemctl enable supervisor.service  
  
# Install Jupyter  
RUN conda install jupyter  
RUN mkdir /notebook/  
RUN jupyter notebook --generate-config  
  
# Start jupyter using systemd  
COPY init/tools_config/jupyter_notebook_config.py
/root/.jupyter/jupyter_notebook_config.py  
COPY init/systemd/jupyter.service /etc/systemd/system/jupyter.service  
RUN systemctl enable jupyter.service  
  
# install requirement for flask  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY init/python/requirements.txt /app/requirements.txt  
RUN /miniconda/bin/pip install -r requirements.txt  
RUN conda install -c conda-forge uwsgi  
  
EXPOSE 80 8080 9001  
CMD [ "/sbin/init" ]

