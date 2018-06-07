FROM wielandbrendel/jupyter-notebook:ubuntu-14.04  
MAINTAINER Wieland Brendel <wieland.brendel@posteo.de>  
  
# From https://github.com/ogrisel/docker-sklearn-openblas  
ADD numpy-site.cfg /tmp/numpy-site.cfg  
ADD scipy-site.cfg /tmp/scipy-site.cfg  
  
ADD build_scipy_stack.sh /tmp/build_scipy_stack.sh  
RUN bash /tmp/build_scipy_stack.sh  
  
## Extremely basic test of install  
RUN python2 -c "import matplotlib, scipy, numpy, pandas, sklearn, seaborn, yt,
patsy, sympy, IPython, statsmodels"  
  
# Clean up from build  
RUN rm -f /tmp/build_scipy_stack.sh /tmp/numpy-site.cfg /tmp/scipy-site.cfg  

