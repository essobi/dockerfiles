# Dockerfile to build environment with python2 and opencv2  
FROM debian:stable  
MAINTAINER Andrey Alekseenko <al42and@gmail.com>  
  
# apt-get first  
RUN apt-get update  
RUN apt-get install -qy \  
cmake \  
git \  
libopencv-dev \  
python-dev \  
python-opencv \  
python-numpy \  
python-scipy \  
python-matplotlib \  
python-pandas \  
python-pip \  
python-setuptools \  
wget \  
x11vnc \  
xvfb \  
openssh-server  
  
# Install dev packages for building jupyter  
RUN apt-get install -qy libzmq3-dev  
  
# python libraries  
RUN pip install -U \  
jupyter \  
scikit-learn  
  
# Remove temporary packages  
RUN apt-get purge -qy \  
libzmq3-dev  
  
# Clean-up  
RUN rm -rf /var/lib/apt/lists/*  
# RUN apt-get clean # Not necessary, Debian does that for you  
RUN rm -rf '/root/.cache/pip/'  
  
# Add Tini, seems necessary for jupyter  
ENV TINI_VERSION v0.10.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/bin/tini  
RUN chmod +x /bin/tini  
# Actually, we only need tini for Jupyter, since sshd and x11vnc work anyway  
ENTRYPOINT ["/bin/tini", "--"]  
  
RUN mkdir /app  
  
# Jupyter notebook configuration  
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
COPY run_jupyter /bin/run_jupyter  
RUN chmod +x /bin/run_jupyter  
EXPOSE 9999  
# X11VNC configuration  
RUN mkdir -p /root/.vnc && x11vnc -storepasswd 1234 /root/.vnc/passwd  
COPY run_vnc /bin/run_vnc  
RUN chmod +x /bin/run_vnc  
EXPOSE 5900  
# ssh configuration  
RUN echo 'root:1234' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd  
COPY run_ssh /bin/run_ssh  
RUN chmod +x /bin/run_ssh  
EXPOSE 22  

