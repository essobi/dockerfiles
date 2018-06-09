FROM alpine:3.7  
LABEL maintainer="mike-sino"  
LABEL version="1.0"  
  
# Install GUN libc  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.27-r0" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget "https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
"$LANG" || true && \  
echo "export LANG=$LANG" > /etc/profile.d/locale.sh && \  
apk del glibc-i18n && \  
rm "/root/.wget-hsts" && \  
apk del --purge .build-dependencies && \  
rm "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
apk add --no-cache --virtual=.build-dependencies bash git  
  
# Install miniconda3  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV MINICONDA_VER latest  
ENV MINICONDA Miniconda3-$MINICONDA_VER-Linux-x86_64.sh  
ENV MINICONDA_URL https://repo.continuum.io/miniconda/$MINICONDA  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
wget $MINICONDA_URL -O miniconda.sh && \  
bash miniconda.sh -f -b -p $CONDA_DIR && \  
rm miniconda.sh && \  
$CONDA_DIR/bin/conda update -y conda && \  
conda upgrade -y pip && \  
rm -r "$CONDA_DIR/pkgs/" && \  
conda clean --all  
  
# Install jupyterlab  
RUN conda install -c conda-forge jupyterLab && \  
mkdir /notebook/  
  
# Install jupyterlab extensions based on nodejs and npm  
RUN apk add --no-cache nodejs && \  
jupyter labextension install jupyterlab-drawio && \  
jupyter labextension install @jupyterlab/github  
  
# Install python2 and python3 kernels  
RUN conda create -n python2 python=2.7 ipykernel && \  
source activate python2 && \  
python -m ipykernel install --user --name=python2 --display-name=python2 && \  
source deactivate  
COPY init/python3/requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
# Install Minimal C kernel for jupyter  
RUN apk add --no-cache gcc libc-dev && \  
pip install jupyter-c-kernel && \  
install_c_kernel  
  
# Install mysql kernel for jupyter  
RUN pip install git+https://github.com/shemic/jupyter-mysql-kernel  
  
# Set environment  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
EXPOSE 8888  
CMD [ "/sbin/init" ]  

