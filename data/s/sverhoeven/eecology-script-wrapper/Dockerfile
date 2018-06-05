FROM ubuntu:14.04  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
ENV DB_HOST db.e-ecology.sara.nl  
# when starting celery as non-root it tries to write to /root/.egg_cache,
redirect it to writeable location  
ENV PYTHON_EGG_CACHE /tmp  
# web app port  
EXPOSE 6543  
ENV MATLAB_VERSION 2012a  
ENV EXTJS_VERSION 4.2.1  
RUN apt-get update && apt-get install -y \  
python-dev python-virtualenv \  
wget unzip \  
libpq-dev \  
octave python-numpy python-scipy \  
r-base-dev littler  
  
# R packages  
RUN /usr/share/doc/littler/examples/install.r DBI RPostgreSQL stringr && rm
-rf /tmp/downloaded_packages/ /tmp/*.rds  
  
# Install Matlab runtime environment  
WORKDIR /opt  
RUN mkdir mcr-install && \  
cd mcr-install && \  
wget
http://nl.mathworks.com/supportfiles/MCR_Runtime/R${MATLAB_VERSION}/MCR_R${MATLAB_VERSION}_glnxa64_installer.zip
&& \  
unzip MCR_R${MATLAB_VERSION}_glnxa64_installer.zip && \  
./install -mode silent -agreeToLicense yes -destinationFolder
/opt/MATLAB/MATLAB_Compiler_Runtime && \  
cd .. && \  
rm -rf mcr-install  
  
# Install ExtJS  
RUN wget http://cdn.sencha.com/ext/gpl/ext-${EXTJS_VERSION}-gpl.zip && \  
unzip ext-${EXTJS_VERSION}-gpl.zip && \  
rm -f ext-${EXTJS_VERSION}-gpl.zip  
  
# Install app  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
RUN ln -s /opt/ext-${EXTJS_VERSION}* script_wrapper/static/ext  
  
RUN pip install -r requirements.txt  
RUN python setup.py develop  
# one python package was installed with -rw------- permission, so service can
not be started as www-data user  
#RUN chmod -R +r /usr/local/lib/python2.7/dist-
packages/python_dateutil-2.2-py2.7.egg/EGG-INFO  
# Build html documentation  
RUN cd docs && sphinx-build -b html -d docs/_build/doctrees .
../script_wrapper/static/docs  
  
# web service command  
CMD gunicorn --user www-data --env DB_HOST=$DB_HOST \--paste docker.ini  

