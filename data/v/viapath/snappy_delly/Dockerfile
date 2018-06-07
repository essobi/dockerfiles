FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# delly (clone takes ages, tons of submodule dependencies, use binary)  
RUN mkdir -p /usr/local/pipeline/delly/ && \  
wget --no-verbose -O /usr/local/pipeline/delly/delly
https://github.com/tobiasrausch/delly/releases/download/v0.6.3/delly_v0.6.3_linux_x86_64bit
&& \  
chmod -R 755 /usr/local/pipeline/delly && \  
chown -R snappy:snappy /usr/local/pipeline && \  
ln -s /usr/local/pipeline/delly/delly /usr/local/bin/ && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/delly' /home/snappy/.bashrc  
  
CMD ["/bin/bash"]  

