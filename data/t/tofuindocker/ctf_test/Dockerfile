FROM ubuntu:16.04  
RUN apt-get update -y  
RUN apt-get install -y python-pip python-dev build-essential vim  
RUN pip install --upgrade pip  
RUN groupadd -r hacker_grp && \  
useradd -rm -g hacker_grp hacker_user  
RUN groupadd -r ctf_gplayer && \  
useradd -rm -g ctf_gplayer ctf_player  
WORKDIR /home/ctf_player  
COPY ./ /problems/binary_exploitation  
WORKDIR /problems/binary_exploitation  
RUN gcc -o justno justno.c  
RUN chown hacker_user auth && chown hacker_user flag && chown hacker_user
justno && chown hacker_user justno.c  
RUN chgrp hacker_grp auth && chgrp hacker_grp flag && chgrp hacker_grp justno
&& chgrp hacker_grp justno.c  
RUN chmod 644 auth && chmod 440 flag && chmod 2755 justno && chmod 644
justno.c  
USER ctf_player  
  

