FROM alpine:latest  
MAINTAINER Ian McAllister <ian.mcallister@awbury.com>  
  
  
# From :  
# * https://github.com/show0k/alpine-jupyter-docker  
# Inspired by :  
# * https://github.com/jupyter/docker-stacks  
# * https://github.com/CognitiveScale/alpine-miniconda  
# Install glibc and useful packages  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk --update add \  
bash \  
git \  
curl \  
ca-certificates \  
bzip2 \  
unzip \  
sudo \  
libstdc++ \  
glib \  
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
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
ENV NB_USER jovyan  
ENV NB_UID 1000  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Configure Miniconda  
ENV MINICONDA_VER 4.2.12  
ENV MINICONDA Miniconda3-$MINICONDA_VER-Linux-x86_64.sh  
ENV MINICONDA_URL https://repo.continuum.io/miniconda/$MINICONDA  
ENV MINICONDA_MD5_SUM d0c7c71cc5659e54ab51f2005a8d96f3  
  
# Create jovyan user with UID=1000 and in the 'users' group  
RUN adduser -s /bin/bash -u $NB_UID -D $NB_USER && \  
mkdir -p /opt/conda && \  
chown jovyan /opt/conda  
  
USER jovyan  
  
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
  
USER root  
  
  
# Configure container startup as root  
WORKDIR /home/$NB_USER/work  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD [ "/bin/bash" ]  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER jovyan  

