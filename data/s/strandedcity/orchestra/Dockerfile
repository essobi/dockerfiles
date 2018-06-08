FROM alpine:latest  
MAINTAINER Phil Seaton <phil@phil-seaton.com>  
  
# Install glibc and useful packages  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk --update add \  
nginx \  
dnsmasq \  
bash \  
git \  
curl \  
ca-certificates \  
bzip2 \  
unzip \  
sudo \  
libstdc++ \  
glib \  
nodejs \  
nodejs-npm \  
libxext \  
libxrender \  
tini@testing \  
&& curl "https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub" -o /etc/apk/keys/sgerrand.rsa.pub \  
&& curl -L "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk" -o glibc.apk \  
&& apk add glibc.apk \  
&& curl -L "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-bin-2.23-r3.apk" -o glibc-bin.apk \  
&& apk add glibc-bin.apk \  
&& /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib \  
&& rm -rf glibc*apk /var/cache/apk/*  
  
# Configure environment  
ENV CONDA_DIR=/opt/conda \  
SHELL=/bin/bash \  
NB_USER=jovyan \  
NB_UID=1000 \  
NB_GID=100 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
ENV PATH=$CONDA_DIR/bin:$PATH \  
HOME=/home/$NB_USER  
  
  
COPY fix-permissions.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/fix-permissions.sh  
  
## Create jovyan user with UID=1000 and in the 'users' group  
RUN adduser -s /bin/bash -u $NB_UID -D $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER:$NB_GID $CONDA_DIR && \  
/usr/local/bin/fix-permissions.sh $HOME && \  
/usr/local/bin/fix-permissions.sh $CONDA_DIR  
  
USER $NB_USER  
  
# Configure Miniconda  
ENV MINICONDA_VER 4.3.31  
ENV MINICONDA Miniconda3-$MINICONDA_VER-Linux-x86_64.sh  
ENV MINICONDA_URL https://repo.continuum.io/miniconda/$MINICONDA  
ENV MINICONDA_MD5_SUM 7fe70b214bee1143e3e3f0467b71453c  
  
# Setup jovyan home directory  
RUN mkdir /home/$NB_USER/work && \  
mkdir /home/$NB_USER/.jupyter && \  
mkdir /home/$NB_USER/.local  
  
# Install conda as jovyan  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
curl -L $MINICONDA_URL -o miniconda.sh && \  
echo "$MINICONDA_MD5_SUM miniconda.sh" | md5sum -c - && \  
/bin/bash miniconda.sh -f -b -p $CONDA_DIR && \  
rm miniconda.sh && \  
$CONDA_DIR/bin/conda install --yes conda==$MINICONDA_VER  
  
# Install Python 3 packages  
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to  
# use notebook-friendly backends in these images  
RUN conda install --quiet --yes \  
'notebook=5.3*' \  
'terminado' \  
'ipywidgets' \  
'nomkl' \  
'ipywidgets=7.0*' \  
'pandas=0.19*' \  
'numexpr=2.6*' \  
'matplotlib=2.0*' \  
'scipy=0.19*' \  
'seaborn=0.7*' \  
'scikit-learn=0.18*' \  
'scikit-image=0.12*' \  
# 'sympy=1.0*' \  
'cython=0.25*' \  
'patsy=0.4*' \  
'statsmodels=0.8*' \  
'cloudpickle=0.2*' \  
'dill=0.2*' \  
'numba=0.31*' \  
'bokeh=0.12*' \  
# 'sqlalchemy=1.1*' \  
'hdf5=1.8.17' \  
'h5py=2.6*' \  
# 'vincent=0.4.*' \  
'beautifulsoup4=4.5.*' \  
'protobuf=3.*' \  
'xlrd' && \  
conda remove --quiet --yes --force qt pyqt && \  
conda clean -tipsy && \  
# Activate ipywidgets extension in the environment that runs the notebook
server  
jupyter nbextension enable --py widgetsnbextension --sys-prefix && \  
# Also activate ipywidgets extension for JupyterLab  
# throws an error on my alpine build for some reason..Error executing Jupyter
command 'labextension': [Errno 2] No such file or directory  
# jupyter labextension install @jupyter-widgets/jupyterlab-manager@^0.31.0 &&
\  
npm cache clean --force && \  
rm -rf $CONDA_DIR/share/jupyter/lab/staging  
  
# Install facets which does not have a pip or conda package at the moment  
# On alpine, will require installing git first, I think.  
# apk update && apk upgrade && \  
# apk add --no-cache bash git openssh  
#RUN cd /tmp && \  
# git clone https://github.com/PAIR-code/facets.git && \  
# cd facets && \  
# jupyter nbextension install facets-dist/ --sys-prefix && \  
# rm -rf facets && \  
# fix-permissions $CONDA_DIR  
# Import matplotlib the first time to build the font cache.  
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/  
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \  
/usr/local/bin/fix-permissions.sh /home/$NB_USER  
  
USER root  
  
# Configure dnsmasq to resolve *.orchestradatacience.com urls (all subdomains)
back to the container  
# This will enable a bash script to run a curl request that can get a cookie
that's ready to go in the browser  
# Ie, I can login on the backend using Jupyter's normal authentication
mechanism, and never  
# have to show the user the Jupyter login page / token nonsense  
RUN echo "user=root" >> /etc/dnsmasq.conf && \  
echo "address=/orchestradatascience.com/127.0.0.1" >> /etc/dnsmasq.conf  
  
# The above setup also relies on forwarding port 80 -> 8888 for internal
requests. Note that the container's port 80  
# is NOT exposed! This is nginx strictly as a port forwarder:  
COPY nginx.conf /etc/nginx/  
RUN adduser -D -g 'www' www && \  
mkdir /www && \  
chown -R www:www /var/lib/nginx && \  
chown -R www:www /www && \  
mkdir /run/nginx && \  
touch /run/nginx/nginx.pid  
  
# Add local files as late as possible to avoid cache busting  
COPY getToken.sh \  
getSessionCookie.sh \  
start-notebook.sh \  
start.sh \  
/usr/local/bin/  
COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/  
RUN chown -R $NB_USER:users /home/$NB_USER/.jupyter && \  
chmod +x /usr/local/bin/start-notebook.sh && \  
chmod +x /usr/local/bin/start.sh && \  
chmod +x /usr/local/bin/getSessionCookie.sh && \  
chmod +x /usr/local/bin/getToken.sh  
  
RUN jupyter nbextension install https://rawgit.com/strandedcity/orchestra-
jupyter/master/dist/orchestra.js && \  
jupyter nbextension install https://rawgit.com/strandedcity/orchestra-
jupyter/master/dist/orchestra-libraries.js && \  
jupyter nbextension enable orchestra  
  
EXPOSE 8888 53 53/udp  
  
# Configure container startup as root  
WORKDIR /home/$NB_USER/work  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["start-notebook.sh"]  
  
# start-notebook.sh has been modified to run as a wrapper script  
# it must run as root, but it'll run jupyter as jovyan  
#USER $NB_USER  

