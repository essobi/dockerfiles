FROM ipmb/ubuntu-python-platter:latest as build  
  
ENV LANG C.UTF-8  
ADD . /code  
  
RUN /build.sh /code  
  
FROM ipmb/ubuntu-python-clean:latest  
RUN groupadd -r margie && useradd --uid=1000 --create-home --home-
dir=/srv/margie --no-log-init -r -g margie margie  
COPY \--from=build /dist /dist  
  
USER margie  
  
RUN cd /tmp && tar xvzf /dist/margie-*.tar.gz --strip-components=1 &&
./install.sh /srv/margie && mv data/setup.cfg /srv/margie && rm -rf /tmp/*  
  
ENV PATH="/srv/margie/bin:${PATH}"  
# directory which contains Python module for margie  
WORKDIR /srv/margie/lib/python3.6/site-packages  
CMD uwsgi --ini=/srv/margie/setup.cfg --virtualenv=/srv/margie  

