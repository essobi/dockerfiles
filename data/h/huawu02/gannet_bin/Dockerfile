# Source code in https://github.com/huawu02/Gannet3.0  
# GABA analysis for data collected using the MEGA-PRESS sequence of CNI.  
#  
# Start with the Matlab r2015b runtime container  
FROM vistalab/mcr-v90  
  
# Copy shell script and MCR binary to /bin  
COPY run_Gannet.sh /bin/run_Gannet  
COPY GannetRun /bin/GannetRun  
  
# change permissions  
RUN chmod +rx /bin/run_Gannet  
RUN chmod +x /bin/GannetRun  

