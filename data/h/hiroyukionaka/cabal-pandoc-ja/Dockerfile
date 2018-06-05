FROM ubuntu:16.10  
MAINTAINER Hiroyuki Onaka  
  
RUN apt-get update -y  
RUN apt-get install -y language-pack-ja-base language-pack-ja  
RUN update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja"  
RUN apt-get install -y texlive-luatex pandoc texlive-fonts-recommended
texlive-fonts-extra texlive-lang-japanese  
RUN apt-get install -y pandoc-citeproc  
RUN apt-get install -y curl  
  

