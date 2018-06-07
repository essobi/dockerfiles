FROM tensorflow/tensorflow:1.4.1-gpu-py3  
  
# Arguments  
ARG user=fcrndocker  
ARG uid=1000  
ARG gid=1000  
# Install some dependencies  
RUN apt-get update && apt-get install -y \  
wget\  
git\  
python3-tk\  
sudo\  
vim\  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Setup user  
RUN export uid="${uid}" gid="${gid}" && \  
groupadd -g "${gid}" "${user}" && \  
useradd -m -u "${uid}" -g "${user}" -s /bin/bash "${user}" && \  
passwd -d "${user}" && \  
usermod -aG sudo "${user}"  
  
WORKDIR "/ws"  
RUN chown "${uid}:${gid}" "/ws"  
USER "${uid}"  
# Changes when we update the repo, forces docker to clone the code and not use
cache.  
ADD https://api.github.com/repos/DavidGillsjo/FCRN-
DepthPrediction/git/refs/heads/devel version.json  
#Download code  
RUN git clone -b devel https://github.com/DavidGillsjo/FCRN-
DepthPrediction.git fcrn  
#All users can run the code (in case the --user argument is used at runtime to
have access to data.)  
RUN chmod -R o+rw fcrn  
  
#Model weights  
RUN wget -nv "http://campar.in.tum.de/files/rupprecht/depthpred/NYU_FCRN-
checkpoint.zip" -O "fcrn/tensorflow/m.zip"  
RUN unzip "fcrn/tensorflow/m.zip" -d "fcrn/tensorflow/"  
  
VOLUME data  
VOLUME host_home  
  
# No need for interactive backend in matplotlib  
ENV MPLBACKEND "Agg"  
# Setup entrypoint  
COPY docker-entrypoint.sh /ws/docker-entrypoint.sh  
ENTRYPOINT ["/ws/docker-entrypoint.sh"]  

