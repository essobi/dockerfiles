# gigmade copy of cellprofiler/cellprofiler with mod to freeze cellprofiler
commit  
# Ü ÜÜÜÜÜÜÜÜÜÜÜ  
# Ü ÜÜÜÜÜÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÜ ° ÜÛ² Ü ÜÜÜÛÛÛßßßßßßÛÛÛÛÜ °  
# ßßßßßßÛÛÛ² Ü ßÛÛÛ² ± ÛÛÛ² ÛÛÛ² ° ÛÛÛ² ±  
# ÛÛÛ² ° ÛÛÛ² ß ÛÛÛ² ÛÛÛ² ß ÛÛÛ² ²  
# ÜÜÜÜÜÜÜÛÛÛ²ÜÜÜÜÜÜÛÛÛ² ÜÜÛÛÛÛÛÛÛÛÛÜÜßßÛ²ÜÛÛÛÛÛÛÛÛÛ² ß  
# ÛÛÛßßßßßÛÛÛ²ßßßßßßÛÛÛ²ßßßßßÛÛÛ²ßßßßßßßÜ² Ü ÛÛÛ² Ü  
# ßÜ ÛÛÛ² Ü ÛÛÛ² Ü ÛÛÛ² Ü ÛÛÛ² ² ÛÛÛ² ²  
# ÛÛÛ² ² ÛÛÛ² ² ÛÛÛ² ² ÛÛÛ² ± ÛÛÛ² ±  
# ÛÛÛ² ± ÛÛÛ² ± ÛÛÛ² ± ÛÛÛ² ° ÛÛÛ² °  
# ÛÛÛ² ° ÛÛÛ² ° ÛÛÛ² ° ÛÛÛ² Ü ÛÛÛ² Ü  
# ÜÛÛÛÛÜÜß ÜÛÛÛÛÜÜÜß ÛÛ² ÜÜÛÛÛÛÛÛß ÜÛÛÛÛÛÛßß  
# Üßßßßßßßß Üßßßßßßß ßÛ ß ß [BROAD‘15]  
# Ü ÜÜÜ ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ ÜÜÜ Ü  
#  
# ... Broad Institute of MIT and Harvard ‘15  
#  
# Proudly Present ...  
#  
# ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»  
# ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
# ³ ³  
# ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
# ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼  
# Released at [þþ:þþ] on [þþ/þþ/þþ]  
# ÉÍÍÍÄÄÄÄÄÄÄÄÄÄÄÄÄÄ Ä ÄÄ Ä Ä ú Ä Ä ÄÄ Ä ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÍÍÍ»  
# ³ º  
# ³ [Supplier : 0x00B1........] [Operating System : all.....] ³  
# ³ [Packager : 0x00B1........] [Video : none....] ³  
# ³ [Cracker : none..........] [Audio : none....] ³  
# ³ [Protection : none..........] [Number of Disks : 1.......] ³  
# ú [Type : Dockerfile....] [Rating : ........] ú  
#  
#  
# ú Well, this is a little Dockerfile that have many functions ú  
# for quantifying phenotypes...enjoy.... ú  
#  
# ú ú  
# ³ ³  
# ³ ³  
# ³ ³  
# ³ ³  
# º º  
# ÈÍÍÍÄÄÄÄÄÄÄÄÄÄÄÄÄÄ Ä ÄÄ Ä Ä ú Ä Ä ÄÄ Ä ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÍÍÍ¼  
#  
# Greets: ...  
#  
#  
# - [ BROAD‘15 ] -  
# -0x00B1 [05/06/84]  
FROM ubuntu:14.04  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
cython \  
git \  
openjdk-7-jdk \  
python-h5py \  
python-imaging \  
python-libtiff \  
python-lxml \  
python-matplotlib \  
python-mysqldb \  
python-numpy \  
python-pandas \  
python-pip \  
python-scipy \  
python-skimage \  
python-sklearn \  
python-vigra \  
python-wxgtk2.8 \  
python-zmq \  
xvfb  
WORKDIR /usr/local/src  
RUN git clone https://github.com/CellProfiler/CellProfiler.git  
WORKDIR /usr/local/src/CellProfiler  
RUN git reset --hard 75bf8ffe9caa645d10bfb2573f0844fdd287ef77  
RUN pip install \  
\--editable \  
.  
ENTRYPOINT ["cellprofiler", "--run", "--run-headless"]  
CMD ["--help"]  

