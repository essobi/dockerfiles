FROM lballabio/quantlib-python  
MAINTAINER Patrick Haener <contact@haenerconsulting.com>  
LABEL Description="An Jupyter notebook server with the QuantLib Python module
available"  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt /requirements.txt  
  
RUN pip install --upgrade pip && pip install jupyter && pip install -r
/requirements.txt  
  
ADD notebooks /notebooks  
  
CMD jupyter-notebook --no-browser --ip=0.0.0.0 --port=8888 --notebook-
dir=/notebooks --NotebookApp.token=""  

