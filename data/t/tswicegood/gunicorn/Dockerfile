FROM continuumio/miniconda  
MAINTAINER Travis Swicegood  
EXPOSE 8000  
RUN /opt/anaconda/bin/conda install -c tswicegood --yes "python<3" gevent
gunicorn  
  
# Provide some sane defaults  
ADD config.py /etc/gunicorn/config.py  
  
# Ensure that Python outputs everything that's printed inside  
# the application rather than buffering it.  
ENV PYTHONUNBUFFERED 1  
# Force the use of `/etc/gunicorn/config.py`, but then allow  
# the server to be executed to be controlled by the outside world.  
ENTRYPOINT ["/opt/anaconda/bin/gunicorn", "--config=/etc/gunicorn/config.py"]  
CMD ["server:app"]  

