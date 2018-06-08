FROM tarhan/pylab  
  
COPY requirements.txt /tmp/  
  
RUN mkdir -p /usr/src/app \  
&& apk --no-cache add \  
curl \  
libffi \  
libzmq \  
openssl \  
sqlite-libs \  
&& apk --no-cache add --virtual build-dependencies \  
build-base \  
libffi-dev \  
sqlite-dev \  
zeromq-dev \  
zlib-dev \  
&& cd /tmp/ \  
&& echo "Installing Jupiter Notebook related packages ..." \  
&& pip install --no-cache-dir -r requirements.txt \  
&& echo "Removing buildtime dependencies ... " \  
&& apk del -f build-dependencies \  
&& echo "Setupping Jupyter to be available from outside ..." \  
&& mkdir -p -m 700 /root/.jupyter/ \  
&& echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py
\  
&& echo "Enabling ipyWidgets extension for Jypiter Notebook ... " \  
&& jupyter nbextension enable \--py widgetsnbextension \  
&& python -m ipykernel.kernelspec \  
&& rm -rf /root/.cache \  
&& echo "Installing tiny init system ... " \  
&& curl -L https://github.com/krallin/tini/releases/download/v0.9.0/tini-
static -o tini \  
&& echo "6ca785cbdd4aba639f5b710e9d92d70b5cf6517daad32dd8a812269c7d8d02c9
*tini" | sha256sum -c \  
&& mv tini /usr/local/bin/tini \  
&& chmod +x /usr/local/bin/tini  
  
WORKDIR /usr/src/app  
  
EXPOSE 8888  
ENTRYPOINT ["tini", "--"]  
CMD ["jupyter", "notebook", "--no-browser", "--transport=ipc"]  

