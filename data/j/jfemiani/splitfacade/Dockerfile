FROM ubuntu:latest  
  
# Install Anaconda 3.0  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
ENV PATH /opt/conda/bin:$PATH  
  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh -O
~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh && \  
ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \  
echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \  
echo "conda activate base" >> ~/.bashrc  
  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
# Update to the latest version of anaconda  
RUN conda update -n base conda  
  
# Install jupyter  
RUN conda install -y jupyter matplotlib scipy  
  
# Install flexx  
RUN conda install -y tornado pyzmq  
#RUN conda install -y -c conda-forge flexx pscript webruntume dialite  
RUN conda config --add channels conda-forge  
RUN conda install -y flexx  
  
# Setup vim autocomplete  
ENV TZ="America/New_York"  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update \  
&& apt-get --force-yes install -y curl vim exuberant-ctags git ack-grep vim-
nox \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN pip install pep8 flake8 pyflakes isort yapf  
  
ADD config/.vimrc /root/.vimrc  
RUN timeout 5m vim || true  
  
# Debugging is important for development  
RUN conda install -y ipdb  
  
# In order to test docker networking issues...  
RUN apt-get update && apt-get install -y iputils-ping dnsutils  
  
# Setup EMACS as an IDE with support for debugging  
RUN apt-get update && apt-get install -y emacs25  
ADD config/.emacs.d /root/.emacs.d  
  
# Expose some ports  
EXPOSE 8888  
EXPOSE 8080  
VOLUME /data  
VOLUME /home/root  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]  
  

