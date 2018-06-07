FROM fedora:25  
MAINTAINER info@vlad.eu  
  
ENV USER default  
ENV GROUP default  
ENV HOME /home/default  
ENV TERM xterm  
  
RUN dnf -y install nss_wrapper procps htop mc mlocate wget tar bzip2 \  
git make ed vim \  
iproute hostname net-tools bind-utils telnet \  
libXext libXrender libXtst freetype fontconfig \  
&& dnf clean all  
  
# add developer user  
RUN groupadd -g 1000 ${GROUP} \  
&& useradd -u 1000 -r --gid 1000 -G wheel -m -d ${HOME} -s /bin/bash -c
"Developer user" ${USER} \  
&& chmod -R 755 ${HOME}  
  
# nss wrapper must be called before extending the prompt PS1  
RUN sed '1 a\if [ -e /tmp/passwd ] ; then \n\  
export NSS_WRAPPER_PASSWD=/tmp/passwd \n\  
[ -e /tmp/group ] && export NSS_WRAPPER_GROUP=/tmp/group \n\  
export LD_PRELOAD=/usr/lib64/libnss_wrapper.so \n\  
fi' -i /etc/skel/.bashrc  
  
# add bash-it  
ENV BASH_IT_ENABLE true  
# Lock and Load a custom theme file  
ENV BASH_IT_THEME standard  
# Set this to false to turn off version control status checking within the
prompt for all themes  
ENV SCM_CHECK true  
# Path to the bash it configuration  
ENV BASH_IT /opt/bash-it  
# Downlowd and inject bash-it framework initialization in bash environment  
RUN git clone https://github.com/revans/bash-it.git ${BASH_IT} \  
&& echo '[[ ${BASH_IT_ENABLE} = 'true' ]] && . ${BASH_IT}/bash_it.sh' >>
/etc/skel/.bashrc  
  
COPY entrypoint.sh /entrypoint.sh  
  
WORKDIR /workspace  
  
VOLUME /workspace  
  
CMD [ "/bin/bash" ]  
ENTRYPOINT [ "/entrypoint.sh" ]  

