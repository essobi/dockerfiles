FROM wielandbrendel/jupyter-scipyserver-python2:cuda6.5  
MAINTAINER Wieland Brendel <wieland.brendel@posteo.de>  
  
ADD build_scipy_stack.sh /tmp/build_scipy_stack.sh  
RUN bash /tmp/build_scipy_stack.sh  
  
## Extremely basic test of install  
RUN python3 -c "import matplotlib, scipy, numpy, pandas, sklearn, seaborn, yt,
patsy, sympy, IPython"  

