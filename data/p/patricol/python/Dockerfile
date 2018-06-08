FROM patricol/ubuntu_x11:18.04  
USER root  
  
RUN apt-get update; \  
apt-get install -y \  
python \  
python-pip \  
python3 \  
python3-pip && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
# pip install --no-cache-dir -U pip setuptools  
# Currently breaks pip. https://github.com/pypa/pip/issues/5240  
# Setup Pycharm  
su user -c "umake ide pycharm /home/user/.local/share/umake/ide/pycharm" && \  
su user -c "umake ide pycharm-professional
/home/user/.local/share/umake/ide/pycharm-professional"  
#COPY --chown=user:user extras/*.dockitem
/home/user/.config/plank/dock1/launchers/#Not yet supported by docker hub's
automated builds, which use an outdated version of docker.  
COPY extras/*.dockitem /home/user/.config/plank/dock1/launchers/  
RUN chown -R user:user /home/user/.config/  
  
USER user

