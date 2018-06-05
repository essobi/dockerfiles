FROM continuumio/anaconda  
  
# put code file to /app  
ADD . /app  
  
# install mysql  
RUN apt-get install mysql-server mysql-client -y  
  
# Install dependency  
#RUN pip install -r app/requirements.txt  
RUN conda install mysql -y  
RUN conda install mysql-connector-python -y  
  
# Setup for Jupyter notebook  
ENV TINI_VERSION v0.6.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
# Go to code directory  
WORKDIR app/notes  
  
# Run final command  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]

