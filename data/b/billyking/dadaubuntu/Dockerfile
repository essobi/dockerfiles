FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y iw curl libcurl4-openssl-dev net-tools python-pip
python-dev build-essential g++ at wget git zsh gdb vim tcpdump gcc ssh iperf
libpcap-dev man lsof bridge-utils uml-utilities  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh  
RUN cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
  
RUN git clone git://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-
zsh/custom/plugins/zsh-syntax-highlighting  
RUN pip install --upgrade pip  
RUN pip install --upgrade virtualenv  
RUN pip install requests datetime BeautifulSoup4 pymongo  

