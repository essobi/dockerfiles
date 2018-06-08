# 1 Download base image Ubuntu 18.04  
FROM ubuntu:18.04  
# 2 Manual setups  
RUN mkdir ~/.local  
  
# 3 Install main programs  
RUN apt-get update && apt-get install -y \  
build-essential \  
nano \  
wget \  
git \  
subversion  
  
# 4 Install Coin-Or Linear Programming 1.16  
RUN svn co https://projects.coin-or.org/svn/Clp/stable/1.16
/root/.local/coin_or_linear_programming_1.16  
WORKDIR /root/.local/coin_or_linear_programming_1.16  
RUN \  
./configure -C && \  
make && \  
make test && \  
make install && \  
cp bin/clp /usr/local/bin  
  
# 7 Install LP Solve 5.5.2.5  
WORKDIR /root/.local  
RUN \  
wget
https://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.5/lp_solve_5.5.2.5_exe_ux64.tar.gz
&& \  
mkdir lp_solve_5.5.2.5 && \  
tar -xvzf lp_solve_5.5.2.5_exe_ux64.tar.gz -C lp_solve_5.5.2.5 && \  
rm lp_solve_5.5.2.5_exe_ux64.tar.gz && \  
cp lp_solve_5.5.2.5/lp_solve /usr/local/bin && \  
cp lp_solve_5.5.2.5/libxli_MathProg.so /usr/lib  
  
# 9 Install GLPK 4.65  
WORKDIR /root/.local  
RUN \  
wget http://ftp.gnu.org/gnu/glpk/glpk-4.65.tar.gz && \  
tar -xvzf glpk-4.65.tar.gz && \  
mv glpk-4.65 glpk_4.65 && \  
rm glpk-4.65.tar.gz  
WORKDIR /root/.local/glpk_4.65  
RUN \  
./configure && \  
make && \  
make install && \  
ldconfig  
  
# 13 Get test files  
RUN \  
mkdir /home/test_files && \  
git clone https://github.com/JM-DelaParra/Test-Files.git /home/test_files && \  
rm -r /home/test_files/.git && \  
rm /home/test_files/README.md  
  
# n-2 Install and configure Oh My Zsh (install all with bash first for
compatibility)  
RUN \  
apt-get update && apt-get install -y zsh && \  
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \  
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc && \  
sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="bira"/g' ~/.zshrc && \  
sed -i 's/ git/ z/g' ~/.zshrc && \  
touch ~/.z && \  
/bin/zsh  
  
# n-1 Default directory  
WORKDIR /home  
  
# n Start with zsh  
ENTRYPOINT /bin/zsh  

