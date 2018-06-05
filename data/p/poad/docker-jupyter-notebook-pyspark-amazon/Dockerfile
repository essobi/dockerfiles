FROM poad/docker-spark-amazon:2.2  
MAINTAINER Kenji Saito  
  
ENV SPARK_HOME /usr/local/spark  
  
RUN yum install -y python27-devel gcc pandoc python35-devel python35-libs
python35-setuptools && \  
yum clean all  
  
RUN /usr/bin/easy_install-3.5 pip &&\  
pip3 install --upgrade pip  
  
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install jupyter && \  
pip install notebook && \  
pip install jupyterlab && \  
pip --no-cache-dir install pandas pyspark && \  
pip install py4j jupyter-spark lxml && \  
pip install --upgrade beautifulsoup4 html5lib && \  
jupyter nbextension install --py jupyter_spark && \  
jupyter serverextension enable \--py jupyter_spark && \  
jupyter nbextension enable \--py jupyter_spark && \  
jupyter nbextension enable \--py widgetsnbextension  
  
RUN jupyter notebook --generate-config --allow-root  
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
  
RUN pip install scipy scikit-learn pygments python-sql pyhive && \  
pip3 install scipy scikit-learn pygments pandas pyspark ipykernel ipython
ipython-sql pyhive  
  
COPY bootstrap.sh /etc/bootstrap.sh  
  
RUN chown root.root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
EXPOSE 18080 7077 8888  
ENTRYPOINT ["/etc/bootstrap.sh"]  
  

