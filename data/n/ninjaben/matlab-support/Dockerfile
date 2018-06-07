# ninjaben/matlab-support  
#  
# Create an image with enough dependencies to support a mounted-in matlab.  
#  
# These expect you to define some local information:  
# \- `MATLAB_ROOT` is your matlab installation on the Docker host, perhaps
`/usr/local/MATLAB/R2016a`.  
# \- `MATLAB_LOGS` is optional path on the Docker host to receive Matlab logs,
perhaps `~/matlab-logs`.  
# \- `MATLAB_MAC_ADDRESS` is the MAC address associated with your own Matlab
License, of the form `00:00:00:00:00:00`.  
#  
# Print Matlab command help:  
# docker run --rm -v "$MATLAB_ROOT":/usr/local/MATLAB/from-host -v
"$MATLAB_LOGS":/var/log/matlab --mac-address="$MATLAB_MAC_ADDRESS"
ninjaben/matlab-support  
#  
# Launch Matlab and print version info:  
# docker run --rm -v "$MATLAB_ROOT":/usr/local/MATLAB/from-host -v
"$MATLAB_LOGS":/var/log/matlab --mac-address="$MATLAB_MAC_ADDRESS"
ninjaben/matlab-support -r "version,exit;"  
#  
# Plot a figure and save it as a png in the logs folder:  
# docker run --rm -v "$MATLAB_ROOT":/usr/local/MATLAB/from-host -v
"$MATLAB_LOGS":/var/log/matlab --mac-address="$MATLAB_MAC_ADDRESS"
ninjaben/matlab-support -r "plot(1:10);print('/var/log/matlab/figure.png',
'-dpng');exit;"  
#  
#Thanks to Michael Perry at Stanford for info, inspiration, starter code!  
#  
  
FROM ubuntu:14.04  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
# Matlab dependencies  
RUN apt-get update && apt-get install -y \  
libpng12-dev libfreetype6-dev \  
libblas-dev liblapack-dev gfortran build-essential xorg  
  
# run the container like a matlab executable  
ENV PATH="/usr/local/MATLAB/from-host/bin:${PATH}"  
ENTRYPOINT ["matlab", "-logfile /var/log/matlab/matlab.log"]  
  
# default to matlab help  
CMD ["-h"]  
  

