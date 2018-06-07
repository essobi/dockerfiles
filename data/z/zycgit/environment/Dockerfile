FROM zycgit/environment  
MAINTAINER ZhaoYongChun "zyc@hasor.net"  
# install  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gnupg \  
gnupg2 \  
git \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf ~/.gnupg/  
  
# work  
VOLUME /work  
ENV WORK_HOME /work  
  
# script  
ADD . /usr/share/deployScript  
RUN ln -s /usr/share/deployScript /script \  
&& chmod 755 /script/*.py \  
&& ln -s /script/deploy.py /usr/bin/deploy \  
&& pip install pexpect  
  
ENV git_host "git@git.oschina.net"  
ENV passphrase "123456"  
#ENTRYPOINT [ "/script/deploy.py" ]  
CMD ["/bin/bash"]

