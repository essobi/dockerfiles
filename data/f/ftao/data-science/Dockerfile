FROM python:3.4  
MAINTAINER Tao Fei <filia.tao@gmail.com>  
  
ENV PIP_INDEX_URL "https://pypi.python.org/simple/"  
WORKDIR /workspace  
COPY requirements.txt /workspace  
RUN pip install -i $PIP_INDEX_URL \--no-cache-dir -r requirements.txt && \  
pip install -i $PIP_INDEX_URL \--no-cache-dir feather-format  
  
# Install XGBoost library  
RUN git clone \--recursive https://github.com/dmlc/xgboost && \  
cd xgboost && \  
make -j4 && \  
cd python-package; python setup.py install  
RUN rm -rf xgboost  
  
# Install Tini  
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.9.0/tini
&& \  
echo "faafbfb5b079303691a939a747d7f60591f2143164093727e870b289a44d9872 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
EXPOSE 8888  
ENTRYPOINT ["tini", "--"]  
CMD ["jupyter", "notebook"]  
  
# Add local files as late as possible to avoid cache busting  
COPY jupyter_notebook_config.py /root/.jupyter/  

