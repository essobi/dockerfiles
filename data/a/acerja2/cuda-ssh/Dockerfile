# Start with CUDA base image  
FROM nvidia/cuda:9.0-devel-ubuntu16.04  
MAINTAINER Alex Cerjanic <acerja2@illinois.edu>  
  
# Install OpenSSH, X server and libgtk (for NVIDIA Visual Profiler)  
RUN apt-get update && apt-get install -y \  
openssh-server xdm libgtk2.0-0 \  
cuda-visual-tools-9-0  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Expose SSH port  
EXPOSE 22  
# Add CUDA back to path during SSH  
RUN echo "export PATH=$PATH:/usr/local/cuda/bin" >> /etc/profile  
  
# Turn on X11Forwarding and allow remote X11  
RUN echo "X11Forwarding yes" >> /etc/ssh/sshd_config && \  
echo "X11UseLocalhost no" >> /etc/ssh/sshd_config && \  
touch /root/.Xauthority  
  
# Copy SSH script to set up LD_LIBRARY_PATH  
COPY ssh.sh /opt/  
RUN chmod a+x /opt/ssh.sh  
CMD ["/bin/bash", "/opt/ssh.sh"]  
  
#The MIT License (MIT)  
#  
#Original Work Copyright (c) 2015 Kai Arulkumaran  
#Modified Work Copyright (c) 2018 Alex Cerjanic  
#  
#Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:  
#  
#The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.  
#  
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.  

