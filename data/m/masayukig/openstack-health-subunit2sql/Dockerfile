# for subunit2sql container  
FROM opensuse:latest  
  
WORKDIR /app  
RUN zypper install -y \  
python \  
python-devel \  
python-pip \  
git \  
&& pip install virtualenv \  
&& zypper install -y -t pattern devel_basis \  
&& rm -rf /var/cache/zypp/*  
WORKDIR /app/subunit2sql  
  
# ONBUILD COPY . /app  
RUN virtualenv /venv \  
&& source /venv/bin/activate \  
&& /venv/bin/pip install PyMySql \  
&& git clone https://git.openstack.org/openstack-infra/subunit2sql.git \  
&& cd subunit2sql && /venv/bin/pip install .  
  
RUN mkdir -p /app/etc /app/bin  
COPY ./etc/subunit2sql.conf /app/etc/subunit2sql.conf  
COPY ./bin/migrate.sh /app/bin/migrate.sh  
CMD ["/app/bin/migrate.sh"]  

