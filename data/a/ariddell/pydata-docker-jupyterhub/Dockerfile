FROM jupyter/jupyterhub  
  
# Python 3 version of Thomas Wiecki's pydata jupyterhub container  
MAINTAINER Allen Riddell <allen.riddell@dartmouth.edu>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget libsm6
libxrender1 libfontconfig1  
RUN apt-get install -y python3-numpy python3-scipy python3-pandas
python3-matplotlib  
RUN pip3 install nltk scikit-learn seaborn statsmodels  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Test  
RUN python3 -c "import numpy, scipy, pandas, matplotlib, sklearn, seaborn,
statsmodels, nltk"  

