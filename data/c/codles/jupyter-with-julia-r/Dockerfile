FROM jupyter/notebook  
  
# The following would be required to enable exporting of ipynbs but creates
too large an image for docker hub  
# TODO: how to enable adjustbox without pulling down 3G of data  
RUN apt-get update && apt-get install -y inkscape # For nbconvert to work with
svg  
# RUN apt-get update && apt-get install -y texlive-latex-base # For creating
pdfs via latex  
# RUN apt-get update && apt-get install -y texlive-latex-extra # required for
adjustbox.sty, probably is an easier way  
RUN apt-get clean  
  
# Install MNE http://martinos.org/mne/stable/index.html  
# Tips from http://stackoverflow.com/questions/11114225/installing-scipy-and-
numpy-using-pip  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libpng-dev \  
libblas-dev\  
liblapack-dev\  
libatlas-base-dev\  
gfortran\  
&& apt-get clean  
RUN pip2 install numpy  
RUN pip2 install scipy  
RUN pip2 install sklearn  
RUN pip2 install pandas  
RUN pip2 install matplotlib  
RUN pip2 install -e 'git+https://github.com/mne-tools/mne-python#egg=mne-dev'  
  
# Install new version of R  
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list  
  
# Install R  
# https://github.com/IRkernel/IRkernel  
# http://stackoverflow.com/questions/26445815/error-when-installing-devtools-
package-for-r-in-ubuntu  
# http://stackoverflow.com/questions/20671814/non-zero-exit-
status-r-3-0-1-xml-and-rcurl  
RUN apt-get update && apt-get install -y \  
r-base \  
libzmq3-dev \  
# libcurl4-gnutls-dev \  
# libcurl4-openssl-dev \  
libxml2-dev \  
&& apt-get clean  
  
# Install R packages  
COPY scripts/rpackages.R /sbin/rpackages.R  
RUN chmod +x /sbin/rpackages.R  
RUN /sbin/rpackages.R  
  
# Install Julia  
RUN apt-get update && apt-get install -y software-properties-common  
RUN /usr/bin/add-apt-repository -y ppa:staticfloat/juliareleases  
RUN /usr/bin/add-apt-repository -y ppa:staticfloat/julia-deps  
RUN apt-get update && apt-get install -y \  
julia \  
python3-pip \  
libzmq3 \  
hdf5-tools \  
&& apt-get clean  
RUN pip3 install ipython jinja2 pyzmq tornado  
  
# Install julia packages  
RUN julia --eval 'Pkg.add("IJulia")'  
COPY scripts/juliapackages.jl /sbin/juliapackages.jl  
RUN cat /sbin/juliapackages.jl  
RUN julia /sbin/juliapackages.jl  
  
COPY requirements.txt /tmp/requirements.txt  
RUN ls /tmp  
RUN pip2 install -r /tmp/requirements.txt  
  
WORKDIR "/"  
RUN mkdir /workspace  
  
EXPOSE 8888  
VOLUME /workspace  
  
RUN mkdir /root/.ssh  
VOLUME /root/.ssh  
  
# https://github.com/ipython/ipython/issues/7062  
CMD sh -c "jupyter notebook --ip=*"  
  

