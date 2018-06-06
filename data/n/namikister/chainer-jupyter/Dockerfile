FROM namikister/chainer  
LABEL maintainer "Yuta Namiki <namikister@gmail.com>"  
# Python binary and source dependencies  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
libsqlite3-dev \  
libzmq3-dev \  
pandoc \  
sqlite3 \  
texlive-fonts-recommended \  
texlive-latex-base \  
texlive-latex-extra && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Tini  
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini >
tini && \  
echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Install some dependencies.  
RUN pip2 --no-cache-dir install ipykernel && \  
pip3 --no-cache-dir install ipykernel && \  
\  
python2 -m ipykernel.kernelspec && \  
python3 -m ipykernel.kernelspec && \  
rm -rf /root/.cache  
  
# Move notebook contents into place.  
# ADD . /usr/src/jupyter-notebook  
RUN git clone --branch 4.4.0 https://github.com/jupyter/notebook.git
/usr/src/jupyter-notebook  
  
# Install dependencies and run tests.  
RUN BUILD_DEPS="nodejs-legacy npm" && \  
apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq $BUILD_DEPS && \  
\  
pip3 install --no-cache-dir /usr/src/jupyter-notebook && \  
pip2 install --no-cache-dir widgetsnbextension && \  
pip3 install --no-cache-dir widgetsnbextension && \  
pip3 install --no-cache-dir jupyter_contrib_nbextensions && \  
\  
npm cache clean && \  
apt-get clean && \  
rm -rf /root/.npm && \  
rm -rf /root/.cache && \  
rm -rf /root/.config && \  
rm -rf /root/.local && \  
rm -rf /root/tmp && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $BUILD_DEPS  
  
# Run tests.  
# RUN pip3 install --no-cache-dir notebook[test] && nosetests -v notebook  
# Add a notebook profile.  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
  
ENTRYPOINT ["tini", "--"]  
  
#CMD ["jupyter", "notebook", "--no-browser", "--allow-root"]  
CMD ["jupyter", "notebook", "--no-browser"]  

