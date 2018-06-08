FROM danielak/r-base-docker:latest  
LABEL author="Brian A. Danielak"  
LABEL version="0.1"  
  
# Install pandoc  
RUN curl -sSL https://get.haskellstack.org/ | sh  
RUN stack setup  
# From https://docs.haskellstack.org/en/stable/GUIDE/#downloading-and-
installation  
ENV PATH "/root/.local/bin:$PATH"  
RUN echo $PATH  
RUN stack install pandoc  
RUN stack install pandoc-citeproc  
RUN pandoc --version  
RUN pandoc-citeproc --version  
  
#  
# Install R Packages  
#  
COPY provisioning/r-packages.R /tmp/  
RUN R --vanilla -f /tmp/r-packages.R  
  
#  
# Copy Compilation Scripts and LaTeX template  
#  
COPY compiling/render_manuscript.R /manuscribble/  
COPY compiling/makefile /manuscribble/  
  
#  
# App Entrypoint  
#  
RUN mkdir /root/.checkpoint  
WORKDIR /manuscript  
ENTRYPOINT [ "R", "--vanilla", "--file=/manuscribble/render_manuscript.R", "--
args"]  

