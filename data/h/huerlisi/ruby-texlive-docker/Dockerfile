FROM ruby:2.3  
  
RUN apt-get update --yes ;\  
apt-get install --yes texlive texlive-lang-german texlive-fonts-extra texlive-
latex-extra pdftk ghostscript ;\  
apt-get clean ;\  
rm -rf /var/lib/apt/lists/*  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - ;\  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list' ;\  
apt-get update --yes ;\  
apt-get install --yes google-chrome-stable ;\  
apt-get clean ;\  
rm -rf /var/lib/apt/lists/*  

