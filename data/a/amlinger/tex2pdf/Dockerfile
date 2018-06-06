FROM ubuntu  
  
MAINTAINER Anton Amlinger <anton.amlinger@gmail.com>  
  
# We need wget for installing the texlive "manually", e.g. the install-tl  
# installer requires it. inotify-tools is used for rerunning the compilation  
# command each time the file changes.  
RUN apt-get update -q && apt-get install -yq wget inotify-tools  
  
ADD http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
/texlive/  
RUN tar -xzf /texlive/install-tl-unx.tar.gz -C /texlive/  
  
ADD . /tex-files  
WORKDIR /tex-files  
  
# Install LaTeX (which may be in whateber directory inside texlive).  
RUN /texlive/*/install-tl --profile=/tex-files/installation.profile  
ENV PATH /usr/local/texlive/2015/bin/x86_64-linux/:$PATH  
  
# This could probably be specified in a neater manner in the  
# installation.profile, but its kept here since it's working for now. Installs  
# missing dependencies for my specific tex to compile.  
RUN tlmgr install adjustbox collectbox supertabular titlesec import svg \  
layaureo marvosym xunicode xltxtra textpos  
  
ENTRYPOINT ["/tex-files/entrypoint.sh"]  
  
CMD ["Bye!"]  

