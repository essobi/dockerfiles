from ubuntu  
run apt-get update  
run apt-get install texlive python3 python3-pip latexmk git texlive-latex-
extra texlive-full --yes  
run apt-get install poppler-utils --yes  
run pip3 install gitdb2==2.0.2 GitPython==2.1.3 Jinja2==2.9.6 jsmin==2.2.2
MarkupSafe==1.0 PyPDF2==1.26.0 PyYAML==3.12 smmap2==2.0.2  
run apt-get install poppler-utils --yes  
run mkdir -p /opt/phd_counter  
copy ./src/ /opt/phd_counter/  
CMD /opt/phd_counter/counter_gen.py --config /var/phd_counter/config.yaml  

