FROM alpine:3.4  
RUN apk add --update curl git python vim wget  
ADD https://raw.githubusercontent.com/DeltaWhy/dotfiles/master/.vimrc
/root/.vimrc  
RUN echo -e \\\n | vim +PlugInstall +qall >/dev/null  
CMD /usr/bin/vim  

