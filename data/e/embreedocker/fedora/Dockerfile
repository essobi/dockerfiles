## ======================================================================== ##  
## Copyright 2009-2017 Intel Corporation ##  
## ##  
## Licensed under the Apache License, Version 2.0 (the "License"); ##  
## you may not use this file except in compliance with the License. ##  
## You may obtain a copy of the License at ##  
## ##  
## http://www.apache.org/licenses/LICENSE-2.0 ##  
## ##  
## Unless required by applicable law or agreed to in writing, software ##  
## distributed under the License is distributed on an "AS IS" BASIS, ##  
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. ##  
## See the License for the specific language governing permissions and ##  
## limitations under the License. ##  
## ======================================================================== ##  
FROM fedora:28  
RUN dnf -y install sudo gcc-c++ gdb clang valgrind vim wget python git nc
cmake make tbb-devel freeglut-devel glfw-devel ImageMagick libXmu-devel libXi-
devel  
RUN dnf -y install ispc  
RUN dnf -y install ncurses-compat-libs # required for clang4/5  
  
RUN useradd -ms /bin/bash visuser  
RUN echo "visuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
ENV HOME=/home/visuser  
ADD .ssh $HOME/.ssh  
RUN chown -R visuser $HOME/.ssh  
RUN chgrp -R visuser $HOME/.ssh  
RUN chmod -R og-rwx $HOME/.ssh  
USER visuser  
WORKDIR $HOME  
  
CMD ["/bin/bash"]  

