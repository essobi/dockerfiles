FROM brownman/gitlab  
  
  
ADD . $HOME  
#CMD . $HOME/.bashrc  
  
#RUN git clone \--depth=1 https://github.com/brownman/install_config_test  
#RUN cd install_config_test && chmod u+x travis.sh && ./travis.sh mean  
#RUN sudo chmod 755 $HOME/mean.sh && bash -c $HOME/mean.sh  
#ONBUILD RUN env  
#ONBUILD RUN history  
#ONBUILD RUN apt-get install toilet  
#ONBUILD RUN toilet --gay 'mean.io'  
#CMD netstat -ntpl | grep mongo  
#RUN . ~/.bashrc && cd myApp && ls -l && grunt test  
COPY ./patch/test.js myApp/config/env/test.js  
COPY ./patch/development.js myApp/config/env/development.js  
COPY ./patch/production.js myApp/config/env/production.js  
  
  
#RUN sudo chmod 755 $HOME/ionic.sh && bash -c $HOME/ionic.sh  
#RUN sudo chmod 755 $HOME/phantom.sh && bash -c $HOME/phantom.sh  
  
#CMD [ "/bin/bash" , "netstat -ntlp | grep mongo", "source $HOME/.bashrc",
"source $HOME/.nvm.sh", "cd myApp", "ls -l ", "grunt test" ]  
#CMD [ "/bin/bash" , "source $HOME/.bashrc", "source $HOME/.nvm.sh", "npm
install -g phantomjs" ]  
CMD [ "/usr/bin/env bash" , 'env' ]  
#ONBUILD RUN cd myApp  
#ONBUILD RUN grunt test  

