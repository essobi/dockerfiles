FROM debian:latest  
  
LABEL maintainer="hrvoje.varga@gmail.com"  
LABEL build="docker build -t hvarga/latex-docker ."  
LABEL run.latex-editor="docker run --rm -v ${PWD}:/home/latex/work -e
DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix hvarga/latex-docker"  
LABEL run.drawing-editor="docker run --rm -v ${PWD}:/home/latex/work -e
DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --entrypoint ipe
hvarga/latex-docker"  
LABEL run.bibliography-manager="docker run --rm -v ${PWD}:/home/latex/work -e
DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --entrypoint jabref
hvarga/latex-docker"  
LABEL run.presentation-console="docker run --rm -v ${PWD}:/home/latex/work -e
DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --entrypoint pdfpc
hvarga/latex-docker <PDF_FILE>"  
LABEL run.build-pdf="docker run --rm -v ${PWD}:/home/latex/work -e
DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --entrypoint make
hvarga/latex-docker"  
  
# Install LaTeX.  
RUN apt-get update -q && DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
sudo \  
texlive-full \  
texlive-lang-all \  
texlive-fonts-extra \  
texstudio \  
ipe \  
jabref \  
firefox-esr \  
python-pygments \  
gnuplot \  
make \  
git \  
vim \  
pdfpc  
  
# Remove cached packages.  
RUN rm -rf /var/lib/apt/lists/*  
  
# Add unprivileged user.  
RUN useradd latex --create-home --uid 1000  
  
USER latex  
WORKDIR /home/latex/work  
  
# Set Firefox as a default system web browser  
RUN mkdir -p /home/latex/.local/share/applications  
RUN xdg-mime default firefox-esr.desktop text/html && \  
xdg-mime default firefox-esr.desktop x-scheme-handler/http && \  
xdg-mime default firefox-esr.desktop x-scheme-handler/https && \  
xdg-mime default firefox-esr.desktop x-scheme-handler/about  
  
# Copy the TeXstudio profile configuration into image.  
COPY files/profile.txsprofile /home/latex  
  
# Run TeXstudio with the custom profile configuration.  
ENTRYPOINT ["texstudio", "--ini-file", "/home/latex/profile.txsprofile"]  

