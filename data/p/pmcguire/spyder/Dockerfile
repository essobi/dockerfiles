FROM pmcguire/anaconda:latest  
  
MAINTAINER Patrick McGuire <patrick.mcguire.j@gmail.com>  
  
RUN apt-get update -qy \  
&& apt-get install -qy sudo \  
&& apt-get install -qy \  
libgl1-mesa-glx \  
libsm6 \  
libxrender1 \  
libfontconfig1 \  
&& apt-get clean \  
&& apt-get autoremove -qy \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN conda install spyder  
  
# Solves permission problem when pulling
http://ixday.github.io/post/docker_git_volume/  
RUN git config --system core.logallrefupdates false  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["spyder --new-instance"]

