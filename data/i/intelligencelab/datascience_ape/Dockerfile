# Distributed under the terms of the Modified BSD License.  
# Latest LTS version of Ubuntu (https://store.docker.com/images/ubuntu)  
FROM ubuntu:latest  
  
LABEL maintainer "haobibo@gmail.com"  
  
USER root  
  
ENV SHELL=/bin/bash \  
DEBIAN_FRONTEND=noninteractive \  
LC_ALL=en_US.UTF-8 \  
LC_TYPE=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
CONDA_DIR=/opt/conda \  
PATH=/opt/conda/bin:$PATH \  
HOME_DIR=/root \  
DATA_DIR=/data  
  
COPY work /tmp/work/  
  
RUN cd /tmp && mkdir -p $HOME_DIR $DATA_DIR \  
&& echo "=============================> Install OS libraries and setup some
configurations..." \  
&& apt-get -y update --fix-missing && apt-get -y upgrade \  
&& apt-get -qq install -y --no-install-recommends \  
apt-utils apt-transport-https ca-certificates lsb-release gnupg dirmngr wget
locales sudo \  
&& DISTRO=$(lsb_release -c -s) && ARCH=$(arch) \  
&& echo "deb https://deb.nodesource.com/node_9.x ${DISTRO} main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/node_9.x ${DISTRO} main" >>
/etc/apt/sources.list.d/nodesource.list \  
&& wget -qO- "https://deb.nodesource.com/gpgkey/nodesource.gpg.key" | apt-key
add - \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen \  
&& mv /root/.bashrc /etc/bash_profile \  
&& echo "[ \$BASH ] && [ -f /etc/bash_profile ] && . /etc/bash_profile" >>
/etc/bash.bashrc \  
&& echo "[ \$BASH ] && [ -f /root/.bashrc ] && . /root/.bashrc" >>
/etc/bash.bashrc \  
&& echo "ALL ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& echo "=============================> Install OS libs, Utilities, Python3
(Miniconda3), R, JDK, NodeJS, Jupyter..." \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* && apt-get -y update --fix-
missing && apt-get -y upgrade \  
&& apt-get -qq install -y --no-install-recommends `cat
/tmp/work/install_apt.list | cut -d '#' -f 1` \  
&& apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& wget -qO- "https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-${ARCH}.sh" -O conda.sh && bash /tmp/conda.sh -f -b -p $CONDA_DIR \  
&& conda update -yq -n base conda \  
&& ( type java && type R && R CMD javareconf || true ) \  
&& echo "=============================> Replace conda packages with pip
installed packages and configure conda..." \  
&& pip install -UIq --pre pip setuptools notebook jupyterhub jupyterlab
ipywidgets \  
&& conda config --system --prepend channels conda-forge \  
&& conda config --system --set auto_update_conda false \  
&& conda config --system --set show_channel_urls true \  
&& conda clean -ya \  
&& echo "=============================> Setup Jupyter: Configurations, Enable
JupyterLab view..." \  
&& mkdir -p $CONDA_DIR/etc/jupyter/ && mv
/tmp/work/jupyter_notebook_config.json $CONDA_DIR/etc/jupyter/ \  
&& jupyter serverextension enable --sys-prefix --py jupyterlab \  
&& echo "-----------------------------> Setup Jupyter: Enable ipywidgets
extension..." \  
&& jupyter labextension install @jupyter-widgets/jupyterlab-manager \  
&& jupyter lab build \  
&& echo "-----------------------------> Setup Jupyter: Install Kernel:
Bash..." \  
&& pip install bash_kernel && python -m bash_kernel.install --sys-prefix \  
&& echo "-----------------------------> Setup Jupyter: Install Kernel:
NodeJS..." \  
&& pip2 install setuptools && pip2 install compiler \  
&& npm install -g --unsafe-perm --python=python2 ijavascript \  
&& ijsinstall --install=global \--spec-path=full \  
&& echo "-----------------------------> Setup Jupyter: Install Kernel: R..." \  
&& echo "options(repos=structure(c(CRAN='http://cran.us.r-project.org')))" >>
/etc/R/Rprofile.site \  
&& R -e "install.packages('devtools',quiet=T,clean=T);" \  
&& R -e
"devtools::install_github('IRkernel/IRkernel',quiet=T,clean=T);IRkernel::installspec(user=F)"
\  
&& echo "-----------------------------> Setup Jupyter: Install Kernel: JVM-
based Kernels..." \  
&& pip install beakerx && beakerx install \  
&& echo "=============================> Build and install tini, add starting
scripts, which will be entry point later..." \  
&& wget -qO- "https://github.com/krallin/tini/archive/v0.18.0.zip" -O tini.zip
&& unzip -q /tmp/tini.zip \  
&& cmake /tmp/tini-* && make install && mv /tmp/tini /usr/local/bin/tini \  
&& mv /tmp/work/start-*.sh /usr/local/bin/ && chmod +x /usr/local/bin/* \  
&& echo "=============================> Clean up and display components
version information..." \  
&& ( rm -rf /root/.* /tmp/.* /tmp/* || true ) && cd \  
&& echo "@ Version of Node/NPM:" `node -v` `npm -v` \  
&& echo "@ Version of Java (java/javac):" && java -version && javac -version \  
&& echo "@ Version of R and IRkernel:" && R -e "R.version.string;
installed.packages()['IRkernel','Version']" \  
&& echo "@ Version of Conda & Python:" && conda info && conda list \  
&& echo "@ Version of Jupyter Notebook/JupyterHub/JupyterLab:" `jupyter
notebook --version` `jupyterhub --version` `jupyter lab --version` \  
&& echo "@ Kernel information of Jupyter:" `jupyter kernelspec list` \  
&& echo "@ Version of image: building finished at:" `date` `uname -a`  
  
ENTRYPOINT ["tini", "--"]  
WORKDIR $HOME_DIR  
EXPOSE 8888  
CMD ["/bin/bash", "/usr/local/bin/start-singleuser.sh"]  

