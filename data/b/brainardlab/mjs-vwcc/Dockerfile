# brainardlab/mjs-vwcc  
#  
# This is part of the MatlabJobSupport project.  
# https://github.com/BrainardLab/MatlabJobSupport  
#  
# It builds on mjs-rtb to add the virtual world color constancy project, so
that  
# we can ship those jobs off to the cloud.  
# Here is a sample "docker run" command:  
FROM brainardlab/mjs-rtb  
  
MAINTAINER David Brainard <brainard@psych.upenn.edu>  
  
### Pre-install large toolboxes so that jobs start faster  
WORKDIR /mjs/projects  
RUN git clone https://github.com/BrainardLab/VirtualWorldColorConstancy.git \  
&& chmod -R a+w /mjs/projects/VirtualWorldColorConstancy  
  
### Configure VirtualWorldColorConstancy  
COPY VirtualWorldColorConstancyLocalHook.m
/mjs/toolboxHooks/VirtualWorldColorConstancyLocalHook.m  
  
### start in known dir so that Matlab can find startup.m  
WORKDIR /mjs  

