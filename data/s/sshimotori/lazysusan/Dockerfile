FROM ubuntu:yakkety  
  
  
ARG clingo_src_version="5.2.0"  
ARG mkatoms_src_version="2.16"  
ARG dlv_rsig_src_version="1.8.10"  
ARG ezcsp_src_version="1.7.9-r4024"  
ARG bprolog_bin_version="75"  
ARG swiprolog_apt_version="7.2.3+dfsg-1build2"  
ARG lp_solve_src_major_version="5.5"  
ARG lp_solve_src_patch_version="2.5"  
ARG lp_solve_bin_version="55"  
ARG user_name="docker"  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y \  
cmake \  
flex \  
gcc \  
g++ \  
locales \  
make \  
python-dev \  
python2.7 \  
subversion \  
sudo \  
unzip  
  
RUN echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
RUN useradd -m ${user_name} \  
&& echo "docker:docker" | chpasswd \  
&& echo "${user_name} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${user_name} \  
&& gpasswd -a ${user_name} sudo  
  
USER ${user_name}  
WORKDIR /home/${user_name}  
  
# install gringo+clasp  
# https://github.com/potassco/clingo/archive/v${clingo_src_version}.tar.gz  
ADD clingo-${clingo_src_version}.tar.gz $HOGE  
RUN cmake -H/home/${user_name}/clingo-${clingo_src_version}
-B/home/${user_name}/clingo -DCMAKE_BUILD_TYPE=Release \  
&& cmake --build /home/${user_name}/clingo  
RUN sudo ln -s $HOME/clingo/bin/gringo /usr/local/bin/gringo \  
&& sudo ln -s $HOME/clingo/bin/clingo /usr/local/bin/clingo \  
&& sudo ln -s $HOME/clingo/bin/clasp /usr/local/bin/clasp  
  
# install mkatoms  
# http://www.mbal.tk/mkatoms/Source/mkatoms-${mkatoms_src_version}.tgz  
ADD mkatoms-${mkatoms_src_version}.tgz $HOME  
RUN sudo chown -R ${user_name}:${user_name} mkatoms-${mkatoms_src_version}  
WORKDIR /home/${user_name}/mkatoms-${mkatoms_src_version}  
RUN ./configure && make && sudo make install  
WORKDIR /home/${user_name}  
  
# install dlv_rsig  
# http://www.mbal.tk/ezcsp/dlv_rsig-${dlv_rsig_src_version}.tgz  
ADD dlv_rsig-${dlv_rsig_src_version}.tgz $HOME  
RUN sudo chown -R ${user_name}:${user_name} dlv_rsig-${dlv_rsig_src_version}  
WORKDIR /home/${user_name}/dlv_rsig-${dlv_rsig_src_version}  
RUN ./configure && make && sudo make install  
WORKDIR /home/${user_name}  
  
# install EZCSP  
# http://www.mbal.tk/ezcsp/ezcsp-${ezcsp_src_version}.tgz  
ADD ezcsp-${ezcsp_src_version}.tgz $HOME  
RUN sudo chown -R ${user_name}:${user_name} ezcsp-${ezcsp_src_version}  
WORKDIR /home/${user_name}/ezcsp-${ezcsp_src_version}  
RUN ./configure && make && sudo make install  
WORKDIR /home/${user_name}  
  
# install BProlog  
# http://www.picat-
lang.org/bprolog/download/bp${bprolog_bin_version}_linux64.tar.gz  
# `bp` refers $HOME/BProlog  
ADD bp${bprolog_bin_version}_linux64.tar.gz $HOME  
RUN sudo ln -s $HOME/BProlog/bp /usr/local/bin/bp  
  
# install SWIProlog  
RUN sudo apt-get install -y swi-prolog=${swiprolog_apt_version}  
  
# install lp_solve  
# https://sourceforge.net/projects/lpsolve/  
RUN mkdir lp_solve_${lp_solve_src_version}_dev_ux64  
ADD
lp_solve_${lp_solve_src_major_version}.${lp_solve_src_patch_version}_Python_source.tar.gz
$HOME  
ADD
lp_solve_${lp_solve_src_major_version}.${lp_solve_src_patch_version}_dev_ux64.tar.gz
/home/${user_name}/lp_solve_${lp_solve_src_major_version}/  
ADD
lp_solve_${lp_solve_src_major_version}.${lp_solve_src_patch_version}_dev_ux64.tar.gz
/home/${user_name}/lp_solve_${lp_solve_src_major_version}/lpsolve${lp_solve_bin_version}/bin/ux32  
#
https://sourceforge.net/projects/lpsolve/files/lpsolve/${lp_solve_src_version}/distribution_${lp_solve_src_version}.htm  
ENV LD_LIBRARY_PATH
/home/${user_name}/lp_solve_${lp_solve_src_major_version}/:$LD_LIBRARY_PATH  
WORKDIR /home/${user_name}/lp_solve_5.5/extra/Python  
RUN sudo python2.7 setup.py install  
WORKDIR /home/${user_name}  
  
RUN sudo rm /etc/sudoers.d/${user_name}  
  
CMD /bin/bash  

