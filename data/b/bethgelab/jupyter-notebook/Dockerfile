FROM bethgelab/xserver:cuda7.5-cudnn4  
  
MAINTAINER Bethge Lab <opensource@bethgelab.org>  
  
# Copied from Jupyter/Notebook  
# the first part is already in docker-xserver  
# ---- COPY BEGIN ----  
#  
# ---- MODIFICATION BEGIN ----  
# Not essential, but wise to set the lang  
# Note: Users with other languages should set this in their derivative image  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PYTHONIOENCODING UTF-8  
# ---- MODIFICATION END ----  
# Install Tini  
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini >
tini && \  
echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Install the recent pip release  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python2 get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py && \  
pip2 --no-cache-dir install requests[security] && \  
pip3 --no-cache-dir install requests[security] && \  
rm -rf /root/.cache  
  
# Install some dependencies.  
RUN pip2 --no-cache-dir install ipykernel && \  
pip3 --no-cache-dir install ipykernel && \  
\  
python2 -m ipykernel.kernelspec && \  
python3 -m ipykernel.kernelspec && \  
rm -rf /root/.cache  
  
# ---- MODIFICATION BEGIN ----  
# Move notebook contents into place.  
# ADD . /usr/src/jupyter-notebook  
RUN cd /usr/src/ && git clone \--branch 4.x
https://github.com/jupyter/notebook.git  
RUN mv /usr/src/notebook /usr/src/jupyter-notebook  
# ---- MODIFICATION END ----  
# Install dependencies and run tests.  
RUN BUILD_DEPS="nodejs-legacy npm" && \  
apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq $BUILD_DEPS && \  
\  
pip3 install --no-cache-dir /usr/src/jupyter-notebook && \  
pip2 install --no-cache-dir widgetsnbextension && \  
pip3 install --no-cache-dir widgetsnbextension && \  
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
  
# ---- MODIFICATION BEGIN ----  
# Run tests.  
#RUN pip3 install --no-cache-dir notebook[test] && nosetests -v notebook  
# ---- MODIFICATION END ----  
# Add a notebook profile.  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py  
  
# ---- MODIFICATION BEGIN ----  
#VOLUME /notebooks  
#WORKDIR /notebooks  
WORKDIR $HOME  
# ---- MODIFICATION END ----  
EXPOSE 8888  
ENTRYPOINT ["tini", "--"]  
  
# ---- MODIFICATION END ----  
#CMD ["jupyter", "notebook", "--no-browser"]  
RUN echo "echo \$USER \$USER_NAME \$USER_HOME" >> /usr/local/bin/run  
RUN echo "lastUser=\$(tail -1 /etc/passwd | cut -d: -f1)" >>
/usr/local/bin/run  
RUN echo "'last user' \$lastUser"  
RUN echo "su -c 'jupyter notebook --ip=0.0.0.0 --no-browser --notebook-
dir=\$USER_HOME' \$lastUser" >> /usr/local/bin/run  
CMD bash -C '/usr/local/bin/run'  
# ---- MODIFICATION END ----  
# ---- COPY END ----  

