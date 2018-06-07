FROM r-base:3.4.0  
RUN apt-get update  
  
# Install required pacakages  
RUN apt-get install -y \  
default-jdk \  
libgdal-dev \  
libproj-dev \  
libssl-dev \  
r-cran-rgl \  
mesa-common-dev \  
libglu1-mesa-dev \  
openbox  
  
# Install xorg and suppress the dialogue asking for keyboard layout  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
xorg \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download and unzip muxViz  
RUN wget https://github.com/manlius/muxViz/archive/master.zip && \  
unzip master.zip  
  
# Download required R Packages  
RUN R -e "options('repos'='http://cran.us.r-project.org');
install.packages('devtools'); install.packages('stringi');
install.packages('XML'); install.packages('rgl'); install.packages('sp');
install.packages('rgdal'); install.packages('shiny');
devtools::install_github('trestletech/ShinyDash'); "  
  
WORKDIR /muxViz-master  
VOLUME /muxViz-master/data  
VOLUME /muxViz-master/export  
  
# Copy muxVizGUI.R and remove runApp() call, so that dependencies are loaded
and persisted in the image  
RUN cp muxVizGUI.R initialise.R  
RUN sed -i.bu 's/runApp(getwd())//' initialise.R  
RUN R -e "source('/muxViz-master/initialise.R')"  
  
# Replace line so that muxViz exposes Port 8080 and is accessible from
external machines  
RUN sed -i.bu 's/runApp(getwd())/runApp(getwd(),8080, "false", "0.0.0.0")/'
muxVizGUI.R  
  
EXPOSE 8080  
CMD R -e "options('repos'='http://cran.us.r-project.org');options(rgl.useNULL
= FALSE);source('/muxViz-master/muxVizGUI.R')"  

