FROM kaggle/python:latest

RUN pip install --upgrade plotly

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

COPY jupyter_notebook_config.py /.jupyter/jupyter_notebook_config.py
WORKDIR /tmp/working

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888
CMD ["jupyter", "notebook"]
