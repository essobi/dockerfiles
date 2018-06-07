FROM ubuntu:16.04  
# Make sure the OS is up to date  
RUN apt-get update && apt-get upgrade -y  
  
# Install most basic of things  
RUN apt-get install -y build-essential git curl wget python2.7 python nano
whiptail  
  
# Install nodejs globally  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
  
# Install cloud9  
RUN git clone git://github.com/c9/core.git /root/.c9sdk &&
/root/.c9sdk/scripts/install-sdk.sh  
  
# Install git-aware-prompt  
RUN mkdir ~/.bash && cd ~/.bash && git clone git://github.com/jimeh/git-aware-
prompt.git  
RUN echo 'export GITAWAREPROMPT=~/.bash/git-aware-prompt' >> ~/.bashrc  
RUN echo 'source "${GITAWAREPROMPT}/main.sh"' >> ~/.bashrc  
RUN echo 'export
PS1="\${debian_chroot:+(\$debian_chroot)}\\[\033[01;32m\\]\u@\h\\[\033[00m\\]:\\[\033[01;34m\\]\w\\[\033[00m\\]
\\[$txtcyn\\]\$git_branch\\[$txtred\\]\$git_dirty\\[$txtrst\\]\$ "' >>
~/.bashrc  
  
# Install nvm - to be used by the end user if they need to fine tune their
node version, since nvm will overwrite the nodejs version in interactive
shell.  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash  
  
# Preinstall an nvm version of node, since it allows installation of global
npm dependencies without sudo.  
RUN bash -c "source /root/.nvm/nvm.sh && nvm install 7"  
RUN bash -c "source /root/.nvm/nvm.sh && nvm alias default 7"  
  
# Create workspace directory  
RUN mkdir /root/workspace  
  
# Copy the readme to workspace root  
COPY ./README-new-workspace.md /root/workspace/README.md  
  
EXPOSE 8080  
# Run the entry script  
ENTRYPOINT ["node", "/root/.c9sdk/server.js"]  
CMD ["-w", "/root/workspace", "--port", "8080", "--packed", "--collab", "--
listen", "0.0.0.0", "-a", ":"]  

