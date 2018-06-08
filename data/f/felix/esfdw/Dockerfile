# vim:set ft=dockerfile:  
FROM felix/multicorn:9.6  
ADD docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/  
  
ARG elasticsearch_pip_install_string  
RUN pip install "$elasticsearch_pip_install_string"  
  
RUN mkdir /src  
  
COPY setup.py /src/  
COPY esfdw/ /src/esfdw  
  
# setup.py develop makes it easy to run this with code mounted from here  
# the copy statements above make it possible to use this when built  
RUN cd /src && python setup.py develop  
  
VOLUME ["/src"]  
WORKDIR /src  
  
RUN mkdir /home/postgres && chown postgres: /home/postgres  

