FROM steinwaywhw/docker-texlive  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y curl wget make gnuplot graphviz zsh git imagemagick
python3 python3-pip pdf2svg  
RUN pip3 install --upgrade pip pandocfilters
git+git://github.com/sergiocorreia/panflute.git  
WORKDIR /tmp  
RUN curl -s https://api.github.com/repos/jgm/pandoc/releases/latest | grep
"browser_download_url.*deb" | cut -d : -f 2,3 | tr -d \" | wget -O pandoc.deb
-qi -  
RUN dpkg -i ./pandoc.deb && rm ./pandoc.deb  
RUN apt-get -f install  
  
WORKDIR /tmp  
RUN sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)" || true  
RUN echo "alias python=python3" >> ~/.zshrc  
  
WORKDIR /tmp/src  
ENTRYPOINT zsh  

