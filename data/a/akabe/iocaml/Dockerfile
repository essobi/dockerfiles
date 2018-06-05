FROM akabe/ocaml:alpine3.5_ocaml4.02.3  
  
ENV PATH $PATH:$HOME/.local/bin  
  
RUN sudo apk add --upgrade --no-cache zeromq libffi python3 \  
m4 zeromq-dev libffi-dev python3-dev && \  
\  
pip3 install --user --no-cache jupyter && \  
opam install -y lwt=2.7.1 ounit=2.0.0 ocp-index iocaml-kernel && \  
\  
sudo apk del m4 zeromq-dev libffi-dev python3-dev && \  
find $HOME/.opam -regex '.*\\\\.\\\\(cmt\\\|cmti\\\|annot\\\|byte\\\\)'
-delete && \  
rm -rf $HOME/.cache \  
$HOME/.opam/archives \  
$HOME/.opam/repo/default/archives \  
$HOME/.opam/$OCAML_VERSION/build  
  
COPY .iocamlinit $HOME/.iocamlinit  
COPY .jupyter $HOME/.jupyter  
COPY entrypoint.sh /  
  
RUN eval $(opam config env) && \  
sudo chown opam $HOME/.iocamlinit $HOME/.jupyter && \  
\  
sed -i "s#__IOCAML_EXECUTABLE__#$(which iocaml.top)#"
$HOME/.jupyter/kernel.json && \  
sed -i "s#__IOCAML_LOG__#$HOME/.jupyter/iocaml.log#"
$HOME/.jupyter/kernel.json && \  
jupyter kernelspec install --user --name iocaml-kernel $HOME/.jupyter && \  
\  
sudo rm -rf $HOME/.jupyter/kernel.json  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "jupyter", "notebook" ]  

