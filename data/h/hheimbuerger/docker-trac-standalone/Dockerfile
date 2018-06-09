FROM python:2.7  
# Install  
RUN apt-get update && apt-get install -y supervisor python-subversion  
  
COPY requirements.txt /tmp  
RUN pip install --no-cache-dir -r /tmp/requirements.txt  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# This is just needed because the python-subversion installs its Python
modules (e.g. svn.core) into dist-packages, which by default isn't in the
PYTHONPATH (see https://serverfault.com/questions/388420/python-svn-bindings-
importerror-no-module-named-svn)  
COPY dist-packages.pth /usr/local/lib/python2.7/site-packages/dist-
packages.pth  
  
VOLUME ["/trac", "/svn"]  
  
EXPOSE 80 3690  
CMD ["/usr/bin/supervisord"]  

