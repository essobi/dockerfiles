FROM ipython/scipystack  
  
MAINTAINER IPython Project <ipython-dev@scipy.org>  
  
RUN pip2 install --upgrade google-api-python-client  
RUN pip2 install --upgrade python-gflags  
ENV PYTHONPATH $SDKROOT/platform/bigquery:$PYTHONPATH #not sure if this is
necessary  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
# You can mount your own SSL certs as necessary here  
ENV PEM_FILE /key.pem  
# $PASSWORD will get `unset` within notebook.sh, turned into an IPython style
hash  
ENV PASSWORD Dont make this your default  
ENV USE_HTTP 0  
ADD notebook.sh /  
RUN chmod u+x /notebook.sh  
  
CMD ["/notebook.sh"]  

