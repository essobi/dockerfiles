##############################################################################  
# MBD: fenics-dev  
# - See the README.md for info  
# - TODO: I should derive from a fixed revision known to work  
  
FROM quay.io/fenicsproject/dev-env:latest  
MAINTAINER Miguel de Benito Delgado <m.debenito.d@gmail.com>  
  
ENV home=/home/fenics  
ENV src=$home/local/src  
  
##############################################################################  
# Install necessary tools and python packages  
# - ssh for remote console access and (possibly) port forwarding  
# - Pandoc for PDF export of notebooks (disabled, requires LaTeX)  
# - libclang-dev for rtags  
# - vim for quick editing inside the container  
# - nbimporter: import IPython notebooks as modules  
# - autograd: Automatic differentiation with numpy support  
  
RUN apt-get update && \  
apt-get install --yes --no-install-recommends \  
ssh \  
vim \  
llvm \  
gdb \  
libclang-dev && \  
rm -rf /var/lib/apt/lists/* && \  
pip3 install --no-cache-dir nbimporter && \  
pip3 install --no-cache-dir autograd && \  
pip3 install --no-cache-dir jupyterthemes && \  
pip3 install --no-cache-dir jupyter_contrib_nbextensions && \  
jupyter contrib nbextension install --system && \  
jupyter nbextensions_configurator enable  
  
##############################################################################  
# Setup terminal, editor related stuff and assorted tools  
# - git-prompt.sh for informative terminal prompts in git repos  
# - .inputrc: better navigation of command line history  
# - .vimrc: minimal vim config  
# - .bashrc: extra stuff  
# - emacs' dir-locals for cmake-ide with dolfin  
# - fenics-notebook to start a notebook using `docker exec ...`  
# - fenics-clean: clears caches  
# - ...  
  
# Use copy from context to avoid creating a new image for each build:  
COPY git-prompt.sh $home/.git-prompt.sh  
COPY dot_bashrc_extra /tmp/dot_bashrc_extra  
COPY dot_inputrc $home/.inputrc  
COPY dot_vimrc $home/.vimrc  
COPY fenics-scripts/fenics-* $home/bin/  
COPY dolfin-dir-locals.el $src/dolfin-dir-locals.el  
  
##############################################################################  
# Final setup, enable SSH, fix permissions  
# FIXME  
# - The systemctl call does not start the service automatically  
# - Remember to MANUALLY add your public key to access the container via ssh  
# (the COPY command is disabled because of the automated builds)  
  
RUN /bin/cat /tmp/dot_bashrc_extra >> $home/.bashrc && \  
rm -f /tmp/dot_bashrc_extra && \  
systemctl enable ssh && \  
mkdir -p $home/.ssh && \  
chmod 744 $home/bin/fenics-* && \  
chown -R fenics.fenics $home/.* $home/bin  
#COPY id_rsa.pub $home/.ssh/authorized_keys  
  
##############################################################################  
# Install rtags  
# - (remote) code browsing, completion and checking for emacs  
  
RUN git clone --recursive https://github.com/Andersbakken/rtags.git $src/rtags
&& \  
cd $src/rtags && \  
git checkout tags/v2.10 && \  
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 . && \  
make && \  
make install && \  
make clean  
  
WORKDIR $home  

