FROM ubuntu:14.04  
MAINTAINER Ferran Pegueroles  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
  
RUN apt-get update && \  
apt-get install -qq -y \  
python-pip \  
python-dev \  
python-lxml \  
libldap2-dev \  
unoconv \  
libpq-dev \  
git \  
mercurial \  
npm \  
freetds-dev libsasl2-dev \  
libmysqlclient-dev \  
postgresql-client \  
build-essential \  
libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev
\  
default-jre-headless && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN mkdir -p /var/lib/trytond  
RUN mkdir -p /app  
  
WORKDIR /app/  
  
RUN hg clone https://bitbucket.org/nantic/tryton-tasks tasks  
ADD bootstrap.py /app/tasks/bootstrap.py  
ADD config /app/config  
  
RUN pip install -r tasks/requirements.txt && \  
pip install -r config/requirements.txt && \  
pip install invoke==0.10.1  
  
RUN hg clone -b 3.4 https://bitbucket.org/nantic/trytond-patches patches && \  
rm patches/account_chart_speedup.diff && \  
touch patches/account_chart_speedup.diff && \  
rm patches/sale_shipment_grouping.diff && \  
touch patches/sale_shipment_grouping.diff && \  
rm patches/issue17151002_80001.diff && \  
touch patches/issue17151002_80001.diff  
  
RUN invoke -e bs 3.4 && \  
find /app -name .hg -type d -exec rm -r {} \; -prune  
  
RUN pip install -e /app/proteus/  
  
RUN cd public_data/sao && \  
npm install grunt && \  
npm install && \  
nodejs node_modules/.bin/grunt --force  
  
ADD trytond.conf /etc/trytond.conf  
ADD trytond-logconf.conf /etc/trytond-logconf.conf  
  
VOLUME /var/lib/trytond  
  
EXPOSE 8000 8002  
ADD run.sh /app/  
  
CMD ["/app/run.sh"]  

