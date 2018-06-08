#Dockerfile to generate image to run SOCIB  
#HF Radar Python Script  
#Work from an Ubuntu Image  
FROM ubuntu  
  
#Install Base Packages  
RUN apt-get update \  
&& apt-get install -y python2.7 python-pip git octave texlive-latex-extra vim
latexmk \  
libgeos-dev libgeos-3.5.0 libgeos++-dev wget libfreetype6-dev libpng-dev
libxft-dev gfortran  
  
#Install Octave Packages  
RUN apt-get install -y octave-specfun octave-control octave-general octave-
signal  
  
#Some housekeeping  
RUN apt-get autoclean && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#install python modules  
RUN pip install --upgrade pip \  
&& pip install numpy==1.11.0 netCDF4==1.2.7 matplotlib==1.5.1 pylatex==1.0.0
requests==2.12.4 \  
pandas==0.19.2 pytz==2014.10 scipy==0.17.0 oct2py==3.8.1 windrose==1.6
adjustText==0.6.0  
RUN pip install git+https://github.com/martalmeida/okean.git#egg=okean  
  
#Install Basemap  
RUN wget https://downloads.sourceforge.net/project/matplotlib/matplotlib-
toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz \  
&& tar -xf basemap-1.0.7.tar.gz && cd basemap-1.0.7 && python setup.py install  
  
#Clone HF Radar Script  
#Alter 123456 if necessary to ensure latest version is cloned at build  
RUN echo '123456' >/dev/null && git clone
https://github.com/socib/HFRadarReports  
  
#Build font cache by starting tool with 0 parameters  
RUN python /HFRadarReports/reportGeneratorHFRadar.py  
  
#Define default command ran when started  
WORKDIR "/HFRadarReports"  
ENTRYPOINT ["python","reportGeneratorHFRadar.py"]  

