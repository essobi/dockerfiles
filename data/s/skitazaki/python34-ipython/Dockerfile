FROM python:3.4.2  
MAINTAINER Shigeru Kitazaki <skitazaki@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y curl  
RUN apt-get install -y build-essential  
RUN apt-get install -y libfreetype6-dev libxft-dev  
RUN apt-get install -y gfortran libopenblas-dev liblapack-dev  
  
# Exporting HTML requires either of Node.JS or Pandoc.  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
RUN apt-get clean  
  
# Use `pip` to make sure latest versions.  
RUN pip install pyzmq  
RUN pip install numpy  
RUN pip install matplotlib  
RUN pip install pandas  
RUN pip install scipy  
RUN pip install scikit-learn  
RUN pip install networkx  
RUN pip install bokeh  
RUN pip install XlsxWriter  
RUN pip install Sphinx  
RUN pip install ipython[notebook]  
  
ENV HOME /root  
RUN ipython profile create nbserver  
  
# Install handy extension(s).  
RUN ipython -c "%install_ext
http://raw.github.com/jrjohansson/version_information/master/version_information.py"  
  
# Configure "nbserver" profile  
RUN sed -i \  
-e "s/^# c.NotebookApp.ip = 'localhost'$/c.NotebookApp.ip = '0.0.0.0'/" \  
-e "s/^# c.NotebookApp.port = 8888$/c.NotebookApp.port = 8888/" \  
-e "s;^# c.NotebookApp.notebook_dir = '/.*'$;c.NotebookApp.notebook_dir = '/notebook';" \  
-e "s/^# c.NotebookApp.open_browser = True$/c.NotebookApp.open_browser = False/" \  
-e "s/^# c.IPKernelApp.matplotlib = None$/c.IPKernelApp.matplotlib = 'inline'/" \  
-e "s/^# c.IPKernelApp.extensions = \\[\\]$/c.IPKernelApp.extensions = ['version_information']/" \  
/root/.ipython/profile_nbserver/ipython_notebook_config.py  
  
# For IPython Notebook to share resources with other containers.  
EXPOSE 8888  
VOLUME ["/notebook"]  
  
WORKDIR /notebook  
# Use shell form to work with notebook.  
CMD ipython notebook --profile=nbserver  

