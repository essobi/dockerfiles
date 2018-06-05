FROM ubuntu  
  
MAINTAINER Audris Mockus <audris@mockus.org>  
  
USER root  
  
#mongodb  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" > /etc/apt/sources.list.d/mongodb-org-3.0.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9ECBEC467F0CEB10  
  
#cran mirro  
RUN echo "deb http://mirror.las.iastate.edu/CRAN/bin/linux/ubuntu xenial/" >
/etc/apt/sources.list.d/cran.list  
#RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
RUN apt-get update && \  
apt-get install -y \  
locales \  
libzmq3-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
libopenblas-base \  
openssh-server \  
lsof sudo \  
fonts-dejavu \  
sssd \  
sssd-tools \  
vim \  
git \  
npm \  
curl lsb-release \  
vim-runtime tmux zsh zip build-essential \  
mariadb-client \  
mariadb-common \  
mongodb-org-shell \  
graphviz \  
r-base-core \  
r-recommended \  
r-base-dev \  
r-cran-car \  
r-cran-rcolorbrewer \  
r-cran-fastcluster \  
python3-dev \  
# ipython3 \  
# ipython3-notebook \  
python3-tk \  
python3-pip \  
python3-yaml python3-msgpack \  
libgmp3-dev \  
libv8-dev  
  
#Google Cloud  
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
RUN apt-get update && \  
apt-get install -y google-cloud-sdk  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
RUN pip3 install --upgrade pip  
RUN pip3 install requests ipython jupyter scikit-learn scikit-image gensim
seaborn nltk beautifulsoup4 pymongo \  
pydot nxpd Tweepy xmltodict flask retrying psycopg2 dulwich click  
#For flask  
#RUN pip3 install virtualenv  
RUN echo "install.packages(c('RecordLinkage','caret','arules', 'pcalg',
'TraMineR','Hmisc','ggplot2','ggmap', 'repr', 'IRdisplay', 'evaluate',
'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest', 'RSentiment',
'wordcloud','tm','bnlearn'), repos='https://mirror.las.iastate.edu/CRAN')" | R
--vanilla  
RUN echo
"devtools::install_github(c('IRkernel/IRkernel','mongosoup/rmongodb'))" | R
--vanilla  
RUN echo "IRkernel::installspec(user = FALSE)" | R --vanilla  
RUN echo 'devtools::install_github("mkearney/rtweet")' | R --vanilla  
RUN echo 'devtools::install_github("igraph/rigraph")' | R --vanilla  
RUN echo "setRepositories(ind=c(2));
source('https://bioconductor.org/biocLite.R');
biocLite('gRain',suppressUpdates=TRUE,ask=FALSE);biocLite('Rgraphviz',suppressUpdates=TRUE,ask=FALSE);"
| R --vanilla  
  
#RUN echo "install.packages('tm',repos='https://mirror.las.iastate.edu/CRAN')"
| R --vanilla  
#RUN mkdir -p /usr/local/share/jupyter/kernels/ipython3  
#COPY kernel.json kernel.js /usr/local/share/jupyter/kernels/ipython3/  
ENV LC_ALL=C  
  
# R pre-requisites  
# mariadb-client mariadb-common mongodb-org-shell mysql-common sqlite3  
# libxrender1 inkscape \  
#install ldap authentication to use utk's ldap  
RUN python3 -m nltk.downloader -d /usr/share/nltk_data stopwords wordnet
gutenberg words  
COPY eecsCA_v3.crt /etc/ssl/  
COPY sssd.conf /etc/sssd/  
COPY common* /etc/pam.d/  
RUN chmod 0600 /etc/sssd/sssd.conf /etc/pam.d/common*  
RUN if [ ! -d /var/run/sshd ]; then mkdir /var/run/sshd; chmod 0755
/var/run/sshd; fi  
  
#install docker-machine  
RUN curl -L https://github.com/docker/machine/releases/download/v0.7.0/docker-
machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine  
  
COPY init.sh startsvc.sh startshell.sh notebook.sh startDef.sh /bin/  
  
ENV NB_USER jovyan  
ENV NB_UID 1000  
ENV HOME /home/$NB_USER  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && mkdir $HOME/.ssh &&
chown -R $NB_USER:users $HOME  
COPY id_rsa_gcloud.pub $HOME/.ssh/authorized_keys  
RUN chown -R $NB_USER:users $HOME && chmod -R og-rwx $HOME/.ssh  
  
RUN set -x \  
&& git clone https://github.com/mrd1no/poster-0.8.1-for-Python-3.4 /src/poster
\  
&& (cd /src/poster && python3 setup.py install)  
RUN pip3 install unirest  
  
#To install git-lfs on DockerImages  
RUN wget "https://github.com/github/git-lfs/releases/download/v1.4.4/git-lfs-
linux-amd64-1.4.4.tar.gz"  
RUN tar -xzf git-lfs-linux-amd64-1.4.4.tar.gz  
RUN cd git-lfs-1.4.4 && ./install.sh  

