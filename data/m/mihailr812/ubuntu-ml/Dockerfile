#  
# Ubuntu Dockerfile  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Pull base image.  
FROM ubuntu:15.10  
MAINTAINER Mihail Raichenko  
  
# Install.  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
  
#RUN apt-add-repository ppa:couchdb/dev -y  
#RUN apt-get update  
#RUN apt-get install couchdb couchdb-bin couchdb-common -y  
RUN \  
apt-get -y update && apt-get -y upgrade && \  
apt-get install -y build-essential software-properties-common && \  
apt-get install -y php5-cli byobu curl git htop man unzip vim wget golang
python2.7 g++ libboost-dev libboost-all-dev cmake \  
mysql-client mongodb-clients libmongo-client-dev libmysqlclient-dev\  
libatlas-base-dev libsvm-dev libsvm-tools libsvm3 python-numpy python-pandas
python-scikits-learn ipython-notebook && \  
apt-get install -y erlang-dev erlang-manpages erlang-base-hipe erlang-eunit
erlang-nox erlang-xmerl erlang-inets \  
libmozjs185-dev libicu-dev libtool libcurl4-openssl-dev \  
python-software-properties python g++ make libgtk2.0 r-base-dev checkinstall
gdebi-core sudo r-base \  
openjdk-7-jre gtk2.0 wget chromium-browser firefox supervisor openssh-server
apt-file python-setuptools git  
  
RUN echo 'install.packages("rpart.plot",
repos="http://cran.us.r-project.org")'|R --no-save  
RUN echo 'install.packages("rattle", repos="http://cran.us.r-project.org")'|R
--no-save  
RUN R -e "install.packages('shiny', repos='https://cran.rstudio.com/')"  
  
# Add files.  
ADD root/.bashrc /root/.bashrc  
ADD phraug /root/phraug  
RUN mkdir build  
RUN git clone https://github.com/JohnLangford/vowpal_wabbit.git
/build/vowpal_wabbit  
WORKDIR /build/vowpal_wabbit  
RUN git checkout 8.1.1  
#ADD vowpal_wabbit /build/vowpal_wabbit  
RUN ./configure --prefix=/usr --with-boost-libdir=/usr/lib/x86_64-linux-gnu &&
make && checkinstall -y  
#RUN R -e "install.packages('xgboost', repos='https://cran.rstudio.com/')"  
ADD fix_empty_rxgboost.patch /build  
#ADD xgboost /build/xgboost  
RUN git clone https://github.com/dmlc/xgboost.git /build/xgboost  
WORKDIR /build/xgboost  
RUN git checkout 0.47  
RUN patch -p1 < ../fix_empty_rxgboost.patch  
RUN make  
RUN R -e "install.packages('knitr', repos='http://cran.us.r-project.org')"  
RUN R -e "install.packages('data', repos='http://cran.us.r-project.org')"  
RUN R -e "install.packages('data.table',
repos='http://cran.us.r-project.org')"  
RUN R -e "install.packages('rmarkdown', repos='http://cran.us.r-project.org')"  
RUN make Rbuild && R CMD INSTALL xgboost_0.4-2.tar.gz  
  
#RUN checkinstall -y  
#WORKDIR /build/xgboost/python-package  
#RUN make  
#RUN export PYTHONPATH=/build/xgboost/wrapper &&\  
# python setup.py install  
#RUN ls /build/xgboost/python-package/xgboost/libxgboostwrapper.so  
#RUN python setup.py install  
RUN make python  
WORKDIR /build/xgboost/python-package  
RUN python setup.py install  
  
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
D68FA50FEA312927  
RUN apt-get update && \  
apt-get install -y mongodb-org  
  
#ADD root/.gitconfig /root/.gitconfig  
#ADD root/.scripts /root/.scripts  
VOLUME ["/shared_data"]  
  
# Set environment variables.  
ENV HOME /root  
  
WORKDIR /tmp  
RUN wget https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.4.2.786-amd64.deb  
RUN gdebi -n shiny-server-1.4.2.786-amd64.deb  
RUN rm shiny-server-1.4.2.786-amd64.deb  
  
RUN easy_install pip && pip install luigi  
RUN apt-get update && apt-get install -y openjdk-7-jre gtk2.0 wget chromium-
browser firefox supervisor openssh-server apt-file  
  
RUN pip install pymongo  
RUN pip install pyelasticsearch  
CMD ["/bin/bash"]  

