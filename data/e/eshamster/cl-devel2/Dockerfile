FROM eshamster/cl-base:2.3C  
  
RUN apk update --no-cache  
RUN apk add --no-cache emacs git w3m  
  
# --- install wget with certificate --- #  
RUN apk add --no-cache ca-certificates wget openssh && \  
update-ca-certificates  
  
# --- make work directory --- #  
ARG work_dir=/tmp/work  
RUN mkdir ${work_dir}  
  
# --- user settings --- #  
ARG emacs_home=/root/.emacs.d  
ARG site_lisp=${emacs_home}/site-lisp  
ARG emacs_docs=${emacs_home}/docs  
  
ARG dev_dir=/root/work  
  
RUN mkdir ${emacs_home} && \  
mkdir ${site_lisp} && \  
mkdir ${emacs_docs}  
  
RUN ln -s ${HOME}/.roswell/local-projects ${dev_dir}  
  
# --- install HyperSpec --- #  
ARG hyperspec=HyperSpec-7-0  
RUN cd ${work_dir} && \  
wget -O -
ftp://ftp.lispworks.com/pub/software_tools/reference/${hyperspec}.tar.gz | tar
zxf - && \  
mv HyperSpec ${emacs_docs}  
  
# --- install slime-repl-color --- #  
RUN cd ${site_lisp} && \  
wget https://raw.githubusercontent.com/deadtrickster/slime-repl-ansi-
color/master/slime-repl-ansi-color.el  
  
# --- run emacs for installing packages --- #  
# In slime 2.20, slime-restart-inferior-lisp fails when using ccl-bin.  
# If changing lexical-binding in slime.el to nil, it could be solved.  
# But in the settings, it fails when using sbcl-bin...  
# So I decided to downgrade slime to 2.19  
RUN cd ${emacs_home}/site-lisp && \  
wget -O - https://github.com/slime/slime/archive/v2.19.tar.gz | tar zxf - && \  
wget -O - https://github.com/purcell/ac-slime/archive/0.8.tar.gz | tar zxf -  
COPY init.el ${emacs_home}  
  
RUN emacs --batch --load ${emacs_home}/init.el  
  
# --- miscs --- #  
WORKDIR /root  

