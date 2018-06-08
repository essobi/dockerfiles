FROM simphonyproject/ubuntu-14.04-vncapp:v0.5.0  
LABEL eu.simphony-project.docker.ui_name="Simphony Framework (w/ Mayavi)"  
LABEL eu.simphony-project.docker.description="Ubuntu machine with simphony
framework preinstalled"  
  
RUN apt-get update -qq \  
&& apt-get install -y make git \  
&& git clone https://github.com/simphony/simphony-framework.git /tmp/simphony-
framework \  
&& cd /tmp/simphony-framework \  
&& git checkout 0.3.0  
  
# Simphony Framework with mayavi  
WORKDIR /tmp/simphony-framework  
  
# Virtual environments for PYTHONPATH etc.  
ENV SIMPHONYENV /simphony  
  
# Make sure that the virtual environment would be activated on startup  
RUN /bin/bash -c 'echo ". $SIMPHONYENV/bin/activate" >> /etc/skel/.bashrc'  
  
RUN /bin/bash -c 'make deps apt-mayavi-deps venv-prepare \  
&& source /simphony/bin/activate \  
&& make simphony simphony-mayavi' \  
&& rm -rf /var/lib/apt/lists/*  
  
# The Openfoam Ubuntu prebuilt package installs the library in  
# /root/OpenFOAM/-2.3.1/platforms/linux64GccDPOpt/lib  
# which is not accessible by the user, they need to be copied over  
RUN cp -rf /root/OpenFOAM/-2.3.1/platforms/linux64GccDPOpt/lib/*
$SIMPHONYENV/lib  
  
# Examples files for simphony mayavi  
# and put it on the Desktop  
RUN apt-get update -qq \  
&& apt-get install -y unzip \  
&& wget https://github.com/simphony/simphony-
mayavi/releases/download/0.4.0/examples.zip -O /tmp/simphony-
framework/examples.zip \  
&& unzip /tmp/simphony-framework/examples.zip \  
&& mkdir -p /etc/skel/Desktop \  
&& mv examples /etc/skel/Desktop/  
  
WORKDIR /tmp  
RUN rm -rf /tmp/simphony-framework  
  
# Setup preference for loading simphony-mayavi plugin in Mayavi2  
RUN mkdir -p /etc/skel/.enthought/mayavi_e3  
COPY container-files/preferences.ini /etc/skel/.enthought/mayavi_e3/  
  
# Autostart Mayavi2  
# Create directory for openbox user's config  
RUN mkdir -p /etc/skel/.config/openbox  
RUN /bin/bash -c 'echo "(eval `cat $SIMPHONYENV/bin/activate` && mayavi2
-style cleanlooks) &" > /etc/skel/.config/openbox/autostart'  
RUN chmod 755 /etc/skel/.config/openbox/autostart  

