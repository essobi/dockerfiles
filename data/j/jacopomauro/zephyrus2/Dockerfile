FROM python:2-stretch  
MAINTAINER Jacopo Mauro  
  
# install required python packages  
RUN pip install \  
antlr4-python2-runtime \  
psutil \  
click  
  
# download and install zephyurs2  
RUN cd / && \  
mkdir solvers_exec && \  
cd /solvers_exec && \  
git clone --recursive --depth=1
https://jacopomauro@bitbucket.org/jacopomauro/zephyrus2.git && \  
pip install -e /solvers_exec/zephyrus2  
  
# MiniSearch not supported anymore -> the new version is bugged  
###############  
# download MiniZincIDE and untar  
###############  
RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \  
cd /solvers_exec && \  
wget
https://github.com/MiniZinc/MiniZincIDE/releases/download/2.1.6/MiniZincIDE-2.1.6-bundle-
linux-x86_64.tgz && \  
tar -zxvf MiniZincIDE-2.1.6-bundle-linux-x86_64.tgz && \  
mv /solvers_exec/MiniZincIDE-2.1.6-bundle-linux-x86_64
/solvers_exec/MiniZincIDE && \  
rm -rf MiniZincIDE-2.1.6-bundle-linux-x86_64.tgz  
  
ENV PATH /solvers_exec/MiniZincIDE:$PATH  
  
###############  
# download or-tools and handle global def  
###############  
RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \  
cd /solvers_exec && \  
wget https://github.com/google/or-
tools/releases/download/v2015-12/Google.OrTools.flatzinc.Linux64.3393.tar.gz
&& \  
tar -zxvf Google.OrTools.flatzinc.Linux64.3393.tar.gz && \  
rm -rf Google.OrTools.flatzinc.Linux64.3393.tar.gz && \  
ln -s /solvers_exec/or-tools.Linux64/bin/fzn-or-tools /bin/fzn-ortools && \  
( [ -d /solvers_exec/MiniZincIDE ] && \  
ln -s /solvers_exec/or-tools.Linux64/share/minizinc
/solvers_exec/MiniZincIDE/share/minizinc/ortools || \  
echo MiniZincIde not installed ) && \  
( [ -d /solvers_exec/minisearch ] && \  
ln -s /solvers_exec/or-tools.Linux64/share/minizinc
/solvers_exec/minisearch/share/minizinc/ortools || \  
echo MiniSearch not installed )  
  
  
  
###############  
# compile ortools (right now not done, takes too much time)  
###############  
# alias svn="svn --non-interactive --trust-server-cert"  
  
  
###############  
# gecode is already provided by MINIZINC  
# requires MiniZincIDE  
###############  
  
RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \  
###############  
# install needed packages  
###############  
apt-get update && \  
apt-get install -y \  
qt5-default && \  
rm -rf /var/lib/apt/lists/* && \  
[ -d /solvers_exec/minisearch ] && \  
ln -s /solvers_exec/minisearch/share/minizinc/gecode
/solvers_exec/MiniZincIDE/share/minizinc/gecode || \  
echo "Minisearch not detected. Continuing"  
  
  
  
  
###############  
# download fzn2smt  
###############  
  
COPY ./docker_scripts/antlr-runtime-3.2.jar /antlr-runtime-3.2.jar  
  
RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \  
###############  
# install needed packages  
###############  
apt-get update && \  
# openjdk and unzip for the fzn2smt  
apt-get install -y \  
unzip \  
openjdk-8-jdk && \  
rm -rf /var/lib/apt/lists/* && \  
cd /solvers_exec && \  
wget http://ima.udg.edu/recerca/lap/fzn2smt/version/fzn2smt-2-0-02.zip && \  
unzip fzn2smt-2-0-02.zip && \  
rm -rf fzn2smt-2-0-02.zip  
  
ENV CLASSPATH=/solvers_exec/fzn2smt-2-0-02:/antlr-runtime-3.2.jar:$CLASSPATH  
  
  
###############  
# download chuffed, add global-dir in minizinc  
# requires the installation of MiniZincIDE  
###############  
  
COPY ./docker_scripts/fzn-chuffed /bin/fzn-chuffed  
  
RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \  
cd /solvers_exec && \  
git clone --depth=1 https://github.com/geoffchu/chuffed.git && \  
chmod 755 /bin/fzn-chuffed && \  
chmod 755 /solvers_exec/chuffed/binary/linux/fzn_chuffed && \  
( [ -d /solvers_exec/MiniZincIDE ] && \  
ln -s /solvers_exec/chuffed/binary/linux/mznlib
/solvers_exec/MiniZincIDE/share/minizinc/chuffed || \  
echo MiniZincIde not installed ) && \  
( [ -d /solvers_exec/minisearch ] && \  
ln -s /solvers_exec/chuffed/binary/linux/mznlib
/solvers_exec/minisearch/share/minizinc/chuffed || \  
echo MiniSearch not installed )  
  
###############  
# download and compile z3  
###############  
RUN ( [ -d /solvers_exec ] || mkdir /solvers_exec ) && \  
###############  
# install needed packages  
###############  
#apt-get update && \  
#apt-get install -y \  
# cmake \  
# bison \  
# flex && \  
#rm -rf /var/lib/apt/lists/* && \  
cd /solvers_exec && \  
###############  
# install z3  
###############  
git clone --depth 1 https://github.com/Z3Prover/z3.git && \  
cd z3 && \  
python scripts/mk_make.py --python && \  
cd build && \  
make && \  
make install  
  
  
  
  
EXPOSE 9001  
WORKDIR /solvers_exec/zephyrus2/zephyrus2  
CMD ["python", "server.py"]  
  
  

