FROM ubuntu:16.04  
MAINTAINER Ben Lyall <ben@lyall.me>  
  
USER root  
  
# install python  
RUN apt-get update && \  
apt-get install -y --no-install-recommends python3 \  
python3-pip \  
python3-dev \  
python3-pandas \  
python3-numpy \  
python3-scipy \  
python3-nltk \  
python3-setuptools \  
python \  
python-pip \  
python-dev \  
python-pandas \  
python-numpy \  
python-scipy \  
python-nltk \  
python-setuptools \  
wget \  
apt-transport-https \  
sudo  
  
# install jupyter for python 2  
RUN pip install jupyter  
  
# install jupyter for python 3  
RUN pip3 install jupyter  
  
# setup kernels  
RUN ipython2 kernel install  
RUN ipython3 kernel install  
  
# now let's install R  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN echo "deb http://cran.csiro.au/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y r-base \  
r-base-dev  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
# Install Tini  
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.9.0/tini
&& \  
echo "faafbfb5b079303691a939a747d7f60591f2143164093727e870b289a44d9872 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# create a user to run things as  
RUN useradd -m -s /bin/bash -N -u 1000 jupyter && \  
mkdir /home/jupyter/.jupyter  
  
# add the user to sudo  
RUN echo "jupyter ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/notebook  
  
# create a place to store the notebooks  
USER jupyter  
RUN mkdir /home/jupyter/notebooks  
  
# setup some other stuff that will come in handy  
USER root  
EXPOSE 8888  
WORKDIR /home/jupyter/notebooks  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
# start-notebook.sh starts the server, so copy it and the jupyter notebook
config  
COPY start-notebook.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/start-notebook.sh  
COPY jupyter_notebook_config.py /home/jupyter/.jupyter/  
RUN chown -R jupyter:users /home/jupyter/.jupyter  
  
# time to setup the R kernel for jupyter  
# install dependencies, these seem to cover what we need  
RUN apt-get -y build-dep libcurl4-gnutls-dev  
RUN apt-get -y install libcurl4-gnutls-dev  
  
# actually build and install the kernel  
COPY installRKernel.R /home/jupyter/  
RUN /usr/bin/Rscript /home/jupyter/installRKernel.R  
  
USER jupyter  

