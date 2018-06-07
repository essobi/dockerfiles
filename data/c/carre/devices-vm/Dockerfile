FROM ubuntu:14.04  
MAINTAINER Nick Portokallidis <portokallidis@gmail.com>  
  
  
# ======================== VIRTUOSO INSTALLATION
================================#  
# Install Virtuoso prerequisites  
RUN apt-get update \  
&& apt-get install -y build-essential debhelper autotools-dev autoconf
automake unzip wget net-tools git libtool flex bison gperf gawk m4 libssl-dev
libreadline-dev libreadline-dev openssl  
  
# Set Virtuoso commit SHA to Virtuoso 7.2.4 release (25/04/2016)  
ENV VIRTUOSO_COMMIT 96055f6a70a92c3098a7e786592f4d8ba8aae214  
  
# Get Virtuoso source code from GitHub and checkout specific commit  
# Make and install Virtuoso (by default in /usr/local/virtuoso-opensource)  
RUN git clone https://github.com/openlink/virtuoso-opensource.git \  
&& cd virtuoso-opensource \  
&& git checkout ${VIRTUOSO_COMMIT} \  
&& ./autogen.sh \  
&& CFLAGS="-O2 -m64" && export CFLAGS && ./configure --disable-bpel-vad
--enable-conductor-vad --disable-dbpedia-vad --disable-demo-vad --disable-
isparql-vad --disable-ods-vad --disable-sparqldemo-vad --disable-syncml-vad
--disable-tutorial-vad --with-readline --program-transform-
name="s/isql/isql-v/" \  
&& make && make install \  
&& ln -s /usr/local/virtuoso-opensource/var/lib/virtuoso/ /var/lib/virtuoso \  
&& ln -s /var/lib/virtuoso/db /data \  
&& cd .. \  
&& rm -r /virtuoso-opensource  
  
# Add Virtuoso bin to the PATH  
ENV PATH /usr/local/virtuoso-opensource/bin/:$PATH  
  
  
  
# ======================== PYTHON INSTALLATION
================================#  
# python and relevant tools  
RUN apt-get update && apt-get install -y \  
build-essential \  
apache2 \  
python \  
python-dev \  
libxml2-dev \  
libxslt-dev \  
libssl-dev \  
zlib1g-dev \  
libyaml-dev \  
libffi-dev \  
python-pip  
  
# General dev tools  
RUN apt-get install -y git && pip install --upgrade pip virtualenv requests  
  
# ======================== DJANGO INSTALLATION
================================#  
RUN apt-get update && apt-get install -y \  
gcc \  
gettext \  
mysql-client libmysqlclient-dev \  
postgresql-client libpq-dev \  
sqlite3 \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
ENV DJANGO_VERSION 1.9.7  
RUN pip install mysqlclient psycopg2 django=="$DJANGO_VERSION"  
  
# ======================== CONFIGURATION ================================#  
# Add Virtuoso config  
ADD virtuoso.ini /virtuoso.ini  
  
# Add dump_nquads_procedure  
ADD dump_nquads_procedure.sql /dump_nquads_procedure.sql  
  
# Add Virtuoso log cleaning script  
ADD clean-logs.sh /clean-logs.sh  
  
# Add startup script  
ADD virtuoso.sh /virtuoso.sh  
  
VOLUME /data  
WORKDIR /data  
EXPOSE 8890  
EXPOSE 1111  
EXPOSE 80  
CMD ["/bin/bash", "/virtuoso.sh"]  

