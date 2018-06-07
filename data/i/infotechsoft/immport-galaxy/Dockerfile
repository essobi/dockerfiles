# ==================================  
# infotechsoft/immport-galaxy  
# ----------------------------------  
# 2018-01-05  
# thomas@infotechsoft.com  
# ==================================  
# TODO - Add/Configure Postgres  
# TODO - Update Galaxy Configuration  
# TODO - Configure HTTPS  
# TODO - Add/Configure Ansible  
# TODO - Add/Configure HTCondor  
# TODO - Reduce image size  
FROM debian:9-slim  
  
LABEL name="infotechsoft/immport-galaxy" \  
release-date="2018-01-05" \  
description="ImmPortGalaxy on Debian" \  
immportgalaxy.url="https://github.com/ImmPortDB/immport-galaxy" \  
maintainer="Thomas J. Taylor <thomas@infotechsoft.com>"  
  
ARG GALAXY_RELEASE  
ARG GALAXY_REPO  
  
ENV DEBIAN_FRONTEND=noninteractive \  
GALAXY_RELEASE=${GALAXY_RELEASE:-master} \  
GALAXY_REPO=${GALAXY_REPO:-https://api.github.com/repos/ImmPortDB/immport-
galaxy/tarball/master} \  
GALAXY_HOME=/home/galaxy \  
GALAXY_USER=galaxy \  
GALAXY_GID=1001 \  
GALAXY_UID=1001 \  
GALAXY_VIRTUAL_ENV=/home/galaxy/.venv \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
PATH=/opt/conda/bin:$PATH  
  
# Configure Locale to en_US.UTF-8  
# Add CRAN repo to get the latest R for Debian (requires `gnupg` for key
management)  
# Update R dependencies (stretch-cran34)  
# Install ImmPort-Galaxy prerequisites  
RUN apt-get -qq update && \  
apt-get -qq -y install \  
locales \  
gnupg && \  
echo "${LANG} UTF-8" | tee -a /etc/locale.gen && \  
locale-gen "${LANG}" && \  
dpkg-reconfigure --frontend $DEBIAN_FRONTEND locales && \  
update-locale "${LANG}"  
RUN echo "deb http://cloud.r-project.org/bin/linux/debian/ stretch-cran34/" |
tee -a /etc/apt/sources.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key
E19F5F87128899B192B1A2C2AD5F960A256A04AF && \  
apt-get -qq update && \  
apt-get -qq -y --no-install-recommends install \  
curl \  
gfortran \  
g++ \  
libbz2-dev \  
libcurl4-openssl-dev \  
libglu1-mesa-dev \  
libhdf5-dev \  
libhdf5-serial-dev \  
liblzma-dev \  
libnlopt-dev \  
libpcre3-dev \  
libreadline-dev \  
libx11-dev \  
libxml2-dev \  
mesa-common-dev \  
python2.7 \  
python-dev \  
python-pip \  
r-base \  
r-base-dev \  
xorg-dev && \  
pip install --upgrade pip && \  
pip install --upgrade virtualenv && \  
apt-get -qq -y autoremove && \  
apt-get -qq -y clean && \  
rm -rf /tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# Add initialization and configuration files  
COPY src/ /tmp/  
  
# Create GALAXY_USER  
# Retrieve the Galaxy source files (ImmPort-Galaxy 16.07)  
RUN mkdir -p $GALAXY_HOME && \  
groupadd -r $GALAXY_USER -g $GALAXY_GID && \  
useradd -u $GALAXY_UID -r -g $GALAXY_USER -d $GALAXY_HOME -c "Galaxy user"
$GALAXY_USER && \  
curl -L $GALAXY_REPO | tar xz -C $GALAXY_HOME \--strip-components 1 && \  
chown -R $GALAXY_USER:$GALAXY_USER $GALAXY_HOME && \  
cp /tmp/galaxy.ini $GALAXY_HOME/config/galaxy.ini  
  
WORKDIR $GALAXY_HOME  
  
# Install required Bioconductor packages  
# Install required python packages in the galaxy virtual environment (.venv):  
RUN Rscript /tmp/r-requirements.R && \  
virtualenv $GALAXY_VIRTUAL_ENV \--distribute && \  
chown -R $GALAXY_USER:$GALAXY_USER $GALAXY_VIRTUAL_ENV && \  
. $GALAXY_VIRTUAL_ENV/bin/activate && \  
pip install -r /tmp/pip-requirements.txt && \  
./scripts/common_startup.sh --no-create-venv --no-replace-pip  
  
# ImmPort Galaxy supports auto-detection of FCS files, with the following
dependency  
RUN curl -o /tmp/anaconda.sh
https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh && \  
/bin/bash /tmp/anaconda.sh -b -p /opt/conda && \  
cp /tmp/.condarc /opt/conda/.condarc && \  
conda update -y --all && \  
conda install -y ig-checkFCS && \  
conda clean -y --tarballs --packages --source-cache && \  
find /opt/conda \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ && \  
apt-get -qq -y autoremove && \  
apt-get -qq -y clean && \  
for x in `ls /usr/share/locale | grep -v -i en | grep -v -i local`; \  
do rm -rf /usr/share/locale/$x; \  
done && \  
rm -rf /tmp/* \  
/usr/share/doc/* \  
/usr/share/man/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# Compile FLOCK. The binaries are included in
$GALAXY_HOME/tools/flowtools/src.  
RUN cd ./tools/flowtools/bin && \  
cc -o flock1 ../src/flock1.c ../src/find_connected.c -lm && \  
cc -o flock2 ../src/flock2.c -lm && \  
cc -o cent_adjust ../src/cent_adjust.c -lm  
  
ENV DEBIAN_FRONTEND=newt  
  
EXPOSE 8080  
USER $GALAXY_USER  
  
# Initializes and starts up Galaxy  
CMD ["sh", "run.sh"]

