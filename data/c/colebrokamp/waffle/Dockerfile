FROM ubuntu:16.04  
LABEL maintainer="Cole Brokamp <cole.brokamp@gmail.com>"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM screen-256color  
  
RUN apt-get update && apt-get install -yqq \  
locales \  
software-properties-common \  
&& apt-get clean  
  
# Set locale to UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8 && /usr/sbin/update-locale
LANG=$LANG  
  
RUN add-apt-repository -y ppa:neovim-ppa/stable  
RUN add-apt-repository -y ppa:opencpu/jq  
RUN apt-get update && apt-get install -yqq --no-install-recommends \  
autoconf \  
build-essential \  
curl \  
git \  
tmux \  
vim \  
python-dev \  
python-pip \  
python3-dev \  
python3-pip \  
python3-setuptools \  
neovim \  
wget  
  
# RUN pip install --no-cache-dir --upgrade pip  
# RUN pip install --no-cache-dir --upgrade setuptools  
# RUN pip install --no-cache-dir --upgrade neovim  
RUN pip3 install -U --no-cache-dir --upgrade pip  
RUN pip3 install -U --no-cache-dir --upgrade setuptools  
RUN pip3 install -U --no-cache-dir --upgrade neovim  
  
RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/ " >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
RUN apt-get update \  
&& apt-get install -yqq --no-install-recommends \  
libcurl4-openssl-dev \  
libssl-dev \  
libgdal-dev \  
libgeos-dev \  
libproj-dev \  
liblwgeom-dev \  
libudunits2-dev \  
libcairo2-dev \  
protobuf-compiler \  
libprotobuf-dev \  
libjq-dev \  
libv8-3.14-dev \  
r-base-dev \  
&& apt-get clean  
  
# set default CRAN repo and DL method  
RUN echo 'options(repos=c(CRAN = "https://cran.rstudio.com/"),
download.file.method="libcurl")' >> /etc/R/Rprofile.site  
  
RUN R -e "install.packages('remotes')"  
RUN R -e "remotes::install_github('cole-brokamp/CB')"  
RUN R -e "remotes::install_github('cole-brokamp/automagic')"  
# R -e "remotes::install_github('cole-brokamp/aiR')" # needs key  
RUN R -e "remotes::install_github('cole-brokamp/OfflineGeocodeR')"  
RUN pip install usaddress # needed for hamilton  
RUN R -e "remotes::install_github('cole-brokamp/hamilton')"  
RUN R -e "remotes::install_github('cole-brokamp/rize')"  
RUN R -e "remotes::install_github('cole-brokamp/aiRpollution')"  
  
RUN R -e "remotes::install_github('jalvesaq/colorout')"  
RUN R -e "remotes::install_github('jimhester/lookup')"  
  
RUN R -e "install.packages('lintr')"  
RUN R -e "install.packages('tidyverse')"  
  
RUN R -e "install.packages('sf')"  
RUN R -e "install.packages('tigris')"  
RUN R -e "install.packages('tidycensus')"  
  
RUN R -e "install.packages('mapview')"  
RUN R -e "install.packages('tmap')"  
  
RUN R -e "install.packages('ranger')"  
  
# install rice interpreter for R  
RUN pip install --no-cache-dir --upgrade rice  
  
# make dirs so singularity won't warn on startup  
RUN mkdir /users  
RUN mkdir /scratch  
  
WORKDIR /root  
COPY . /root/dotfiles  
RUN ./dotfiles/install.sh  
  
ENTRYPOINT [ "/bin/bash" ]  

