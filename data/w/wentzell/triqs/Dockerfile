# Use an official Python runtime as a base image  
FROM ubuntu:17.04  
# Set the working directory to /root  
WORKDIR /root  
  
# Copy the current directory contents into the container at /app  
ADD pkglst /root  
  
# Install required packages as specified in pkglst  
RUN apt-get update  
RUN apt-get --assume-yes upgrade  
RUN apt-get --assume-yes install $(cat pkglst)  
RUN pip install jupyter  
  
# === INSTALL Codes  
# TRIQS  
run git clone https://github.com/TRIQS/triqs.git /root/triqs.src  
run mkdir /root/triqs.build  
WORKDIR /root/triqs.build  
run cmake -DCMAKE_INSTALL_PREFIX=/root/triqs ../triqs.src  
run make -j 8 && make install  
  
# CTHyb  
run git clone https://github.com/TRIQS/cthyb.git /root/cthyb.src  
run mkdir /root/cthyb.build  
WORKDIR /root/cthyb.build  
run cmake -DTRIQS_PATH=/root/triqs ../cthyb.src  
run make -j 8 && make install  
  
# ctint_tutorial  
run git clone https://github.com/TRIQS/ctint_tutorial.git
/root/ctint_tutorial.src  
run mkdir /root/ctint_tutorial.build  
WORKDIR /root/ctint_tutorial.build  
run cmake -DTRIQS_PATH=/root/triqs ../ctint_tutorial.src  
run make -j 8 && make install  
  
# Tutorial notebooks  
run mkdir /root/notebooks  
ADD *.ipynb /root/notebooks/  
run git clone https://github.com/TRIQS/tutorials.git /root/notebooks/tutorials  
WORKDIR /root/notebooks  
  
# Remove build directories and sources  
# run rm -rf /root/*.build  
# run rm -rf /root/*.src  
# ================  
# Make port 8888 available to the world outside this container  
EXPOSE 8888  
# Start the notebook when the container launches.  
ENV PYTHONPATH /root/triqs/lib/python2.7/dist-packages:$PYTHONPATH  
CMD jupyter notebook --no-browser --port 8888 --ip=* --allow-root
--NotebookApp.token='' \--NotebookApp.password=''  

