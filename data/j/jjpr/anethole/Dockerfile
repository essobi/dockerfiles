FROM jjpr/blender-mayavi-jupyter:latest  
  
RUN apt-get update && \  
apt-get install -y \  
texlive  
  
RUN apt-get update && \  
apt-get install -y \  
texlive-latex-extra  
  
RUN apt-get update && \  
apt-get install -y \  
dvipng  
  
RUN apt-get update && \  
apt-get install -y \  
imagemagick  
  
COPY Equation_To_Object_Instructions.ipynb /data/examples/  
  
RUN mkdir /data/examples/images  
COPY images/ruffle_equation.png /data/examples/images/  
COPY images/wrapped_ruffle.png /data/examples/images/  
COPY images/printed.png /data/examples/images/  
COPY images/saddle_grapher.png /data/examples/images/  
  
RUN mkdir /data/tools  
COPY solidify.py /data/tools/  
COPY solidify_x3d.py /data/tools/  
  

