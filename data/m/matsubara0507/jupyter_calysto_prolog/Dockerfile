FROM python:3  
RUN pip install ipython jupyter metakernel  
ADD . /root/calysto_prolog  
WORKDIR /root/calysto_prolog  
RUN python setup.py install  
RUN cd kernels && jupyter kernelspec install calysto_prolog  
  
WORKDIR /root/notebook  
  
CMD ["jupyter", "notebook", "--allow-root", "--no-brows", "--ip='*'"]  

