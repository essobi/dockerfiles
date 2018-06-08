FROM simphonyproject/ubuntu-12.04-vncapp:v0.5.0  
LABEL eu.simphony-project.docker.ui_name="Simphony Framework (w/ Paraview)"  
LABEL eu.simphony-project.docker.description="Ubuntu machine with simphony
framework preinstalled (with paraview)"  
  
RUN apt-get update -qq \  
&& apt-get install -y make git lsb-release software-properties-common python-
software-properties \  
&& add-apt-repository 'deb http://us.archive.ubuntu.com/ubuntu/ precise
multiverse' \  
&& apt-get update -qq \  
&& apt-get install -y libcgal8 libcgal-dev \  
&& git clone https://github.com/simphony/simphony-framework.git /tmp/simphony-
framework \  
&& cd /tmp/simphony-framework \  
&& git checkout 0.3.0  
  
# Virtual environments for PYTHONPATH etc.  
ENV SIMPHONYENV /simphony  
  
WORKDIR /tmp/simphony-framework  
  
# Make sure that the virtual environment would be activated on startup  
RUN /bin/bash -c 'echo ". $SIMPHONYENV/bin/activate" >> /etc/skel/.bashrc'  
  
RUN /bin/bash -c 'make deps apt-paraview-deps venv-prepare \  
&& source $SIMPHONYENV/bin/activate \  
&& make simphony simphony-paraview' \  
&& rm -rf /var/lib/apt/lists/*  
  
# The Openfoam Ubuntu prebuilt package installs the library in  
# /root/OpenFOAM/-2.3.0/platforms/linux64GccDPOpt/lib  
# which is not accessible by the user, they need to be copied over  
RUN cp -rf /root/OpenFOAM/-2.3.0/platforms/linux64GccDPOpt/lib/*
$SIMPHONYENV/lib  
  
# Examples files for simphony paraview  
# and put it on the Desktop  
RUN apt-get update -qq \  
&& apt-get install -y unzip \  
&& wget https://github.com/simphony/simphony-
paraview/releases/download/0.2.0/examples.zip -O /tmp/simphony-
framework/examples.zip \  
&& unzip /tmp/simphony-framework/examples.zip \  
&& mkdir -p /etc/skel/Desktop \  
&& mv examples /etc/skel/Desktop/  
  
WORKDIR /tmp  
RUN rm -rf /tmp/simphony-framework  
  
# install ipython and qtconsole  
RUN apt-get install -y ipython ipython-qtconsole \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Autostart IPython Qtconsole  
# Create directory for openbox user's config  
RUN mkdir -p /etc/skel/.config/openbox  
RUN /bin/bash -c 'echo ". $SIMPHONYENV/bin/activate; ipython qtconsole" >
/etc/skel/.config/openbox/autostart'  
RUN chmod 755 /etc/skel/.config/openbox/autostart  

