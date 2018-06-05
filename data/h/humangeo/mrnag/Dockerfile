FROM debian:latest  
COPY . /tmp/mrnag  
RUN apt-get update \  
&& apt-get install -y emacs-nox \  
&& export MRNAG_VERSION=$(sed -n 's/(define-package "mrnag"
"\\([0-9.]*\\)"/\1/p' /tmp/mrnag/mrnag-pkg.el) \  
&& tar -cvf /tmp/mrnag-$MRNAG_VERSION.tar --transform
"s,^tmp/mrnag,mrnag-$MRNAG_VERSION," /tmp/mrnag \  
&& emacs -batch --eval "(package-install-file
\"/tmp/mrnag-$MRNAG_VERSION.tar\")" \  
&& apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm
/tmp/mrnag-$MRNAG_VERSION.tar  
CMD ["emacs", "--batch", "--execute", "(package-initialize)", "--funcall",
"mrnag-launcher"]  

