FROM centos:6  
LABEL maintainer="conda-forge@googlegroups.com"  
  
# Set an encoding to make things work smoothly.  
ENV LANG en_US.UTF-8  
# Add a timestamp for the build. Also, bust the cache.  
ADD http://tycho.usno.navy.mil/timer.html /opt/docker/etc/timestamp  
  
# Resolves a nasty NOKEY warning that appears when using yum.  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6  
  
# Install basic requirements.  
RUN yum update -y && \  
yum install -y bzip2 \  
patch \  
sudo \  
tar \  
which && \  
yum clean all  
  
# give sudo permission for conda user to run yum (user creation is postponed  
# to the entrypoint, so we can create a user with the same id as the host)  
RUN echo 'conda ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Install the latest Miniconda with Python 3 and update everything.  
RUN curl -s -L
https://repo.continuum.io/miniconda/Miniconda3-4.3.31-Linux-x86_64.sh >
miniconda.sh && \  
openssl md5 miniconda.sh | grep 7fe70b214bee1143e3e3f0467b71453c && \  
bash miniconda.sh -b -p /opt/conda && \  
rm miniconda.sh && \  
touch /opt/conda/conda-meta/pinned && \  
export PATH=/opt/conda/bin:$PATH && \  
conda config --set show_channel_urls True && \  
conda config --append channels conda-forge && \  
conda update --all --yes && \  
conda clean -tipy  
  
# Install conda build and deployment tools.  
RUN export PATH="/opt/conda/bin:${PATH}" && \  
conda install --yes --quiet conda-build anaconda-client jinja2 setuptools && \  
conda install --yes git && \  
conda clean -tipsy  
  
# Install docker tools.  
RUN export PATH="/opt/conda/bin:${PATH}" && \  
conda install --yes gosu && \  
export CONDA_GOSU_INFO=( `conda list gosu | grep gosu` ) && \  
echo "gosu ${CONDA_GOSU_INFO[1]}" >> /opt/conda/conda-meta/pinned && \  
conda install --yes tini && \  
export CONDA_TINI_INFO=( `conda list tini | grep tini` ) && \  
echo "tini ${CONDA_TINI_INFO[1]}" >> /opt/conda/conda-meta/pinned && \  
conda clean -tipsy  
  
# Environment variables  
ENV USER_ID=9001  
ENV GROUP_ID=9001  
ENV HOME=/home/conda  
ENV USER=conda  
ENV LOGNAME=conda  
ENV MAIL=/var/spool/mail/conda  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/conda/bin  
  
# Create conda user  
RUN groupadd -g $GROUP_ID -o conda && \  
useradd --shell /bin/bash -u $USER_ID -g $GROUP_ID -o -c "" -m conda  
RUN chown -R conda:conda /opt/conda && \  
cp /root/.condarc $HOME/.condarc && \  
chown conda:conda $HOME/.condarc  
RUN cp -R /etc/skel $HOME && \  
chown -R conda:conda $HOME/skel && \  
(ls -A1 $HOME/skel | xargs -I {} mv -n $HOME/skel/{} $HOME) && \  
rm -Rf $HOME/skel  
  
# Add a file for users to source to activate the `conda`  
# environment `root` and the devtoolset compiler. Also  
# add a file that wraps that for use with the `ENTRYPOINT`.  
COPY entrypoint_source /opt/docker/bin/entrypoint_source  
COPY entrypoint /opt/docker/bin/entrypoint  
  
# Ensure that all containers start with tini and the user selected process.  
# Activate the `conda` environment `root` and the devtoolset compiler.  
# Provide a default command (`bash`), which will start if the user doesn't
specify one.  
ENTRYPOINT [ "/opt/conda/bin/tini", "--", "/opt/docker/bin/entrypoint" ]  
CMD [ "/bin/bash" ]  

