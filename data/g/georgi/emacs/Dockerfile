FROM nicferrier/emacsd  
  
ADD . /home/emacs/.emacs.d  
  
RUN rm /home/emacs/.emacs  
  
# RUN /usr/local/emacs/bin/emacs -batch --eval '(package-refresh-contents)'  
RUN /usr/local/emacs/bin/emacs -batch --load /home/emacs/.emacs.d/init.el  

