FROM ubuntu:zesty-20170703  
## base-notebook  
USER root  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install -y wget bzip2 ca-certificates sudo locales fonts-liberation
python3 python3-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
# Install Tini  
RUN wget --quiet
https://github.com/krallin/tini/releases/download/v0.10.0/tini && \  
echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Configure environment  
ENV SHELL /bin/bash  
ENV NB_USER jovyan  
ENV NB_UID 1000  
ENV HOME /home/$NB_USER  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Create jovyan user with UID=1000 and in the 'users' group  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER  
  
USER $NB_USER  
WORKDIR $HOME  
  
# Install Jupyter Notebook and Hub  
RUN pip3 install 'jupyterhub==0.7.2' 'jupyterlab==0.25.2' 'notebook==5.0.0'  
  
## end base-notebook  
## minimal-notobook  
USER root  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
ed \  
emacs \  
git \  
inkscape \  
jed \  
less \  
libsm6 \  
libxext-dev \  
libxrender1 \  
lmodern \  
pandoc \  
python-dev \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-xetex \  
vim \  
unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
## end minimal-notebook  
## r-notebook  
# R pre-requisites  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
fonts-dejavu \  
gfortran \  
gcc \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# R packages. This is different from the docker-stacks r-notebook because we
want R 3.4.1,  
# and there's no way to do that with conda  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties \  
&& add-apt-repository ppa:marutter/rrutter \  
&& apt-get update \  
&& apt-get install -y r-base r-base-dev libssl-dev libcurl4-openssl-dev
libxml2-dev zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
RUN echo "options(repos = c(CRAN = \"https://cran.rstudio.com/\"),
download.file.method = \"libcurl\")" >> .Rprofile \  
&& echo ".libPaths( c( \"~/.R/lib\", .libPaths()) )" >> .Rprofile \  
&& mkdir -p .R/lib  
  
ENV PATH="${PATH}:/home/jovyan/.local/bin"  
RUN R -e "install.packages('devtools')" \  
&& R -e "library(devtools); devtools::install_github('IRkernel/IRkernel');
IRkernel::installspec()" \  
&& R -e "install.packages('plyr')" \  
&& R -e "install.packages('tidyverse')" \  
&& R -e "install.packages('shiny')" \  
&& R -e "install.packages('rmarkdown')" \  
&& R -e "install.packages('forecast')" \  
&& R -e "install.packages('RSQLite')" \  
&& R -e "install.packages('reshape2')" \  
&& R -e "install.packages('nycflights13')" \  
&& R -e "install.packages('caret')" \  
&& R -e "install.packages('RCurl')" \  
&& R -e "install.packages('crayon')" \  
&& R -e "install.packages('randomForest')"  
  
## end r-notebook  
# nbrsessionproxy  
USER root  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libapparmor1 \  
libedit2 \  
psmisc \  
lsb-release \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# You can use rsession from rstudio's desktop package as well.  
ENV RSTUDIO_PKG=rstudio-server-1.0.153-amd64.deb  
  
RUN wget -q http://download2.rstudio.org/${RSTUDIO_PKG}  
RUN dpkg -i ${RSTUDIO_PKG}  
RUN rm ${RSTUDIO_PKG}  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /usr/etc && chmod a+wx /usr/etc && mkdir -p /usr/share/jupyter &&
chmod a+wx /usr/share/jupyter  
  
USER $NB_USER  
  
RUN pip3 install git+https://github.com/ryanlovett/nbserverproxy  
RUN jupyter serverextension enable \--py nbserverproxy  
  
RUN pip3 install git+https://github.com/jupyterhub/nbserverproxy.git  
RUN jupyter serverextension enable \--sys-prefix --py nbserverproxy  
  
RUN pip3 install --no-deps
git+https://github.com/jupyterhub/nbrsessionproxy.git  
RUN jupyter serverextension enable \--sys-prefix --py nbrsessionproxy  
RUN jupyter nbextension install --sys-prefix --py nbrsessionproxy  
RUN jupyter nbextension enable \--sys-prefix --py nbrsessionproxy  
  
# The desktop package uses /usr/lib/rstudio/bin  
ENV PATH="${PATH}:/usr/lib/rstudio-server/bin"  
ENV LD_LIBRARY_PATH="/usr/lib/R/lib:/lib:/usr/lib/x86_64-linux-
gnu:/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server"  
## end nbrsessionproxy  
## scipy-notebook  
USER root  
RUN apt-get update \  
&& apt-get install -y \  
pkg-config \  
libfreetype6-dev \  
libopenblas-dev \  
libav-tools \  
python3-h5py \  
python3-matplotlib \  
python3-numpy \  
python3-scipy \  
python3-pandas \  
python3-sklearn \  
python3-sklearn-pandas \  
python3-seaborn \  
python3-patsy \  
python3-sympy \  
cython3 \  
python3-sqlalchemy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install \  
ipython \  
ipywidgets \  
numexpr \  
statsmodels \  
cloudpickle \  
dill \  
numba \  
bokeh \  
vincent \  
beautifulsoup4 \  
xlrd  
  
RUN jupyter nbextension enable \--py widgetsnbextension --sys-prefix  
  
RUN apt-get update \  
&& apt-get install -y \  
python-pip \  
python-h5py \  
python-matplotlib \  
python-numpy \  
python-scipy \  
python-pandas \  
python-sklearn \  
python-sklearn-pandas \  
python-seaborn \  
python-patsy \  
python-sympy \  
cython \  
python-sqlalchemy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install \  
ipython \  
ipykernel \  
numexpr \  
statsmodels \  
cloudpickle \  
dill \  
numba \  
bokeh \  
vincent \  
beautifulsoup4 \  
xlrd  
  
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/  
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot"  
RUN python2 -m ipykernel install --user  
  
## end scipy-notebooke  
## tensorflow notebook  
RUN pip install -U pip \  
&& pip3 install -U pip \  
&& pip install tensorflow \  
&& pip3 install tensorflow  
  
EXPOSE 8888  
# Configure container startup  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
# Add local files as late as possible to avoid cache busting  
COPY start.sh /usr/local/bin/  
COPY start-notebook.sh /usr/local/bin/  
COPY start-singleuser.sh /usr/local/bin/  
COPY notebook /etc/sudoers.d/  
RUN mkdir -p /etc/jupyter && chown -R $NB_USER:users /etc/jupyter/  
  
USER $NB_USER  

