FROM jupyter/scipy-notebook  
  
MAINTAINER me@alpico.la  
  
USER root  
  
# Install Noto Sans CJK to display Japanese text in matplotlib  
RUN mkdir /tmp/noto && cd /tmp/noto \  
&& wget -q https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-
hinted.zip \  
&& unzip NotoSansCJKjp-hinted.zip \  
&& mkdir -p /usr/share/fonts/opentype/noto \  
# We don't want to install other weight variants (Thin, Light, etc.)  
# because they could be used as default instead of Regular weight  
&& cp NotoSansCJKjp-Regular.otf NotoSansCJKjp-Bold.otf
/usr/share/fonts/opentype/noto/ \  
&& chmod -R a=rX,u+w /usr/share/fonts/opentype/noto/ \  
&& fc-cache -fv \  
&& rm -rf /tmp/noto  
  
USER $NB_UID  
  
# Refresh matplotlib's font cache which the parent image added  
RUN rm /home/$NB_USER/.cache/matplotlib/fontList.py3k.cache  
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot"  

