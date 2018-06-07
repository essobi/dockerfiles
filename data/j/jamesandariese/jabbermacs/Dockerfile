FROM ubuntu:14.04  
RUN apt-get update && apt-get -y install emacs24-nox gnutls-bin && emacs
--batch --eval '(progn (require '"'"'package)(add-to-list '"'"'package-
archives '"'"'("marmalade" . "http://marmalade-repo.org/packages/"))(package-
refresh-contents)(package-install '"'"'jabber))'  
MAINTAINER James Andariese <james@strudelline.net>  
ADD jabber /jabber  
  
CMD /jabber  

