FROM cspinc/datalab-base:latest  
  
# Add R repository  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list  
  
# Add R to Ubuntu Keyring  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \  
&& gpg -a --export E084DAB9 | apt-key add -  
  
# Install R-Base  
RUN apt-get update && apt-get install -y r-base r-base-dev  
  
# Install dependencies for 'tidyverse', then install 'tidyverse'  
RUN apt-get install -y libcurl4-openssl-dev libssl-dev \  
&& R -e "install.packages('tidyverse', repos='https://cran.rstudio.com/')"  
  
# Install (remaining) dependencies for 'rpy2'  
RUN R -e "install.packages(c('RJSONIO','RSQLite','dbplyr'),
repos='https://cran.rstudio.com/')" \  
&& pip3 install rpy2  
  
# Install latest version of rpy2 that works with Python 2.7  
RUN pip install rpy2==2.8.4  
  
# Add files (including shell scripts and notebooks) to the image  
ADD start-jupyter.sh /usr/local/bin/start-jupyter.sh  
ADD authorize_notebook_server.ipynb /usr/local/authenticate-earth-engine.ipynb  
  
# Install the Earth Engine Python API  
RUN pip install earthengine-api && pip3 install earthengine-api  

