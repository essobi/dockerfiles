################################################################################  
# DOCKER IMAGE BUILD FILE  
################################################################################  
FROM louiemenard/vw  
  
MAINTAINER Louie Menard <louie.menard@gmail.com>  
LABEL description="Home Folder"  
LABEL version="1.0"  
  
################################################################################  
# install packages  
################################################################################  
USER root  
RUN yum install -y net-tools  
RUN yum install -y bind  
RUN yum install -y nmap  
  
# install docker  
# RUN yum install -y docker  
# RUN curl -fsSL https://get.docker.com/ | sh  
# RUN usermod -aG docker Louie  
# RUN systemctl enable docker.service  
# RUN systemctl start docker  
  
#install pip, ipython, jupyter  
RUN wget https://bootstrap.pypa.io/get-pip.py -O - | python  
RUN pip install ipython  
RUN pip install jupyter  
  
# install jupyter vim key bindings  
#RUN mkdir -p $(jupyter --data-dir)/nbextensions  
RUN mkdir -p /home/Louie/.local/share/jupyter/nbextensions  
#WORKDIR cd $(jupyter --data-dir)/nbextensions  
WORKDIR mkdir -p /home/Louie/.local/share/jupyter/nbextensions  
RUN git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding  
RUN jupyter nbextension enable vim_binding/vim_binding  
  
# install scipy  
# https://www.scipy.org/install.html  
RUN yum install -y numpy scipy python-matplotlib ipython python-pandas sympy
python-nose atlas-devel  
  
# install sklearn  
# http://scikit-learn.org/stable/install.html  
RUN pip install scikit-learn  
  
  
################################################################################  
# install home folder  
################################################################################  
WORKDIR /home/Louie  
RUN git clone https://github.com/louiemenard/louie.git /home/tmp  
RUN mv /home/tmp/.git /home/Louie/.git  
RUN rm -rf /home/tmp/  
RUN chown -R Louie:Louie *  
RUN chown -R Louie:Louie .*  
  
USER Louie  
RUN git reset --hard HEAD  
#RUN git checkout master  
RUN git pull  
#RUN git submodule update --init --recursive  
RUN git submodule update --init .babun-docker  
RUN git submodule update --init .emacs.d  
RUN git submodule update --init .local/share/jupyter/nbextensions/vim_binding  
RUN git submodule update --init .oh-my-zsh  
RUN git submodule update --init .vim/bundle/conque-term  
RUN git submodule update --init .vim/bundle/vim-ipython  
RUN git submodule update --init .vim/bundle/vim-surround  
RUN git submodule update --init env/docker/centos  
RUN git submodule update --init env/docker/sys  
RUN git submodule update --init env/docker/vw  
#RUN git submodule update --init kaggle  
RUN git submodule foreach git pull origin master  
RUN git submodule foreach git checkout master  
  
################################################################################  
# expose ports  
################################################################################  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8888  
  
################################################################################  
# entry point  
################################################################################  
USER Louie  
WORKDIR /home/Louie  
RUN set -o vi  
ENTRYPOINT /bin/zsh  

