FROM registry.gitlab.com/fdroid/ci-images-server:latest  
  
RUN apt-get update -y && apt-get install -y \  
gettext  
  
#COPY signing-key.asc /  
#RUN gpg --import /signing-key.asc  
# Get repository  
RUN cd / && \  
git clone \--depth 1 https://gitlab.com/fdroid/fdroidserver.git  
  
# Generate mo files  
RUN sed -i -e '/ALL_LINGUAS = de es pt_BR pt_PT tr zh_Hans zh_Hant/s/$/ bo
es_AR fa fr it kab ko nb_NO uk/' /fdroidserver/locale/Makefile  
  
# whatever ... works for me :D  
RUN cd /fdroidserver/locale && make compile || true  
RUN cd /fdroidserver/locale && make compile || true  
RUN cd /fdroidserver/locale && make compile || true  
  
# Install fdroid  
RUN cd /fdroidserver && python3 setup.py install  
  
WORKDIR /repo  

