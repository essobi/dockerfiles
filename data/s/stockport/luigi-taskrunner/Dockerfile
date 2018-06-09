# --------------------------------------------------------------------------  
# This is a Dockerfile to build a Python / Alpine Linux image with  
# luigid running on port 8082  
# --------------------------------------------------------------------------  
FROM python:latest  
  
MAINTAINER Stockport <info@stockport.gov.uk>  
  
ARG user=app  
ARG group=app  
ARG uid=2101  
ARG gid=2101  
# The luigi app is run with user `app`, uid = 2101  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
RUN groupadd -g ${gid} ${group} \  
&& useradd -u ${uid} -g ${group} -m -s /bin/bash ${user}  
  
RUN mkdir /etc/luigi  
ADD ./etc/luigi/logging.cfg /etc/luigi/  
ADD ./etc/luigi/client.cfg /etc/luigi/  
VOLUME /etc/luigi  
  
RUN mkdir /etc/freetds  
ADD ./etc/freetds/freetds.conf /etc/freetds/  
  
RUN mkdir -p /luigi/tasks  
RUN mkdir -p /luigi/work  
RUN mkdir -p /luigi/outputs  
RUN mkdir -p /luigi/inputs  
  
ADD ./luigi/tasks/hello_world.py /luigi/tasks  
  
RUN chown -R ${user}:${group} /luigi  
  
VOLUME /luigi/work  
VOLUME /luigi/tasks  
VOLUME /luigi/outputs  
VOLUME /luigi/inputs  
  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
freetds-dev \  
freetds-bin \  
build-essential \  
libaio1 \  
libaio-dev \  
alien \  
poppler-utils \  
mdbtools \  
unixODBC \  
postgresql-client  
  
# Get Oracle Client (this isn't the offical download location, but at least it
works without logging in!)  
RUN curl -O http://repo.dlt.psu.edu/RHEL5Workstation/x86_64/RPMS/oracle-
instantclient12.1-basic-12.1.0.1.0-1.x86_64.rpm  
RUN curl -O http://repo.dlt.psu.edu/RHEL5Workstation/x86_64/RPMS/oracle-
instantclient12.1-devel-12.1.0.1.0-1.x86_64.rpm  
  
# RPM to DEB  
RUN alien -d *.rpm  
  
# Install packages  
RUN dpkg -i *.deb  
  
# Setup Oracle environment  
RUN echo "/usr/lib/oracle/12.1/client64/lib" > /etc/ld.so.conf.d/oracle.conf  
ENV ORACLE_HOME /usr/lib/oracle/12.1/client64  
ENV LD_LIBRARY_PATH /usr/lib/oracle/12.1/client64/lib  
RUN ldconfig  
  
# Get iconv-chunks  
RUN curl -O https://raw.githubusercontent.com/mla/iconv-chunks/master/iconv-
chunks  
RUN chmod +x iconv-chunks  
RUN mv iconv-chunks /usr/local/bin  
  
USER ${user}  
  
RUN bash -c "pyvenv /luigi/.pyenv \  
&& source /luigi/.pyenv/bin/activate \  
&& pip install cython \  
&& pip install sqlalchemy luigi pymssql psycopg2 alembic pandas xlsxwriter
cx_oracle requests pypdf2"  
  
ADD ./luigi/taskrunner.sh /luigi/  
  
ENTRYPOINT ["bash", "/luigi/taskrunner.sh"]  

