FROM jjpr/blender-mayavi-jupyter:latest  
  
COPY Equation_To_Object_Instructions.ipynb /data/examples/  
  
RUN mkdir /data/examples/images  
COPY images/ruffle_equation.png /data/examples/images/  
COPY images/wrapped_ruffle.png /data/examples/images/  
COPY images/printed.png /data/examples/images/  
COPY images/saddle_grapher.png /data/examples/images/  
  
RUN mkdir /data/tools  
COPY solidify.py /data/tools/  
COPY solidify_x3d.py /data/tools/  
  

