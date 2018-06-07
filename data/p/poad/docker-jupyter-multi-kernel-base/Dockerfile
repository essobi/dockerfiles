FROM poad/docker-jupyter-base:latest  
  
LABEL Kenji Saito "ken-yo@mbr.nifty.com"  
  
ENV PATH ${PATH}:/root/.mix/  
  
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
  
RUN echo $(node --version)  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get purge nodejs -y && apt-get install nodejs -y  
  
# Install Node.js Kernel  
RUN git clone https://github.com/notablemind/jupyter-nodejs.git && \  
cd jupyter-nodejs && \  
mkdir -p ~/.ipython/kernels/nodejs/ && \  
npm install && node install.js && \  
npm run build && \  
npm run build-ext  
  
# Install jupyter-scala & jupyter-kernel  
RUN curl -sL "https://github.com/jupyter-scala/jupyter-
scala/archive/v0.4.2.tar.gz" | tar -xz -C /tmp && \  
cd /tmp && \  
cd jupyter-scala-0.4.2 && \  
cd project && \  
mv build.properties build.properties.bak && \  
sed -e "s/0\\.13\\.15/0.13.17/g" build.properties.bak > build.properties && \  
rm -f build.properties.bak && \  
cd ../ && \  
sbt publishLocal && \  
curl -sL "https://github.com/jupyter-scala/jupyter-
kernel/archive/v0.4.1.tar.gz" | tar -xz -C /tmp &&\  
cd /tmp && \  
cd jupyter-kernel-0.4.1 && \  
cd project && \  
mv build.properties build.properties.bak && \  
sed -e "s/0\\.13\\.15/0.13.17/g" build.properties.bak > build.properties && \  
rm -f build.properties.bak && \  
cd ../ && \  
sbt publishLocal && \  
curl -sL "https://raw.githubusercontent.com/alexarchambault/jupyter-
scala/master/jupyter-scala" -o /root/jupyter-scala.sh && \  
chmod 744 /root/jupyter-scala.sh && \  
sed -e "s/2.11.11/${SCALA_VERSION}/gi" /root/jupyter-scala.sh && \  
/root/jupyter-scala.sh && \  
rm -f /root/jupyter-scala.sh  
  
# # Install Elixir  
RUN cd /root/.local && \  
git clone https://github.com/pprzetacznik/IElixir.git && \  
cd /root/.local/IElixir && \  
mix local.hex --force && \  
mix local.rebar --force && \  
mix deps.get && \  
# mix test && \  
MIX_ENV=prod mix compile && \  
./install_script.sh  
  
# Install ierlang  
RUN cd /root && \  
pip install virtualenv && \  
git clone https://github.com/robbielynch/ierlang.git && \  
git clone http://github.com/zeromq/erlzmq2.git && \  
cd erlzmq2 && \  
make  
# make docs && \  
# make test  
ENV ERL_LIBS /root/erlzmq2:$ERL_LIBS  
ENV PATH $PATH:$ERL_LIBS  
  
  
# Install Rust kernel  
RUN cd /tmp && \  
git clone https://github.com/m0riiiii/jupyter-rust-kernel.git && \  
cd /tmp/jupyter-rust-kernel && \  
jupyter-kernelspec install rust_spec && \  
python3.6 setup.py install  
  
# Install Kotlin kernel  
RUN cd /tmp && \  
git clone https://github.com/ligee/kotlin-jupyter.git && \  
cd kotlin-jupyter && \  
./gradlew install  
  
## Install the Clojure kernel  
ENV CLOJUPYTER_PATH $HOME/clojupyter  
ENV LEIN_ROOT=1  
ENV PATH ${PATH}:/usr/local/bin  
RUN pip install flit && \  
cd /usr/local/bin && \  
wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
&& \  
chmod +x lein && \  
cd /tmp && \  
git clone https://github.com/clojupyter/clojupyter && \  
cd clojupyter && \  
make && \  
make install && \  
mkdir /notebooks  
  
# Install OCaml  
RUN curl -sL "https://github.com/akabe/ocaml-
jupyter/releases/download/v2.2.2/jupyter-2.2.2.tbz" | tar -xj -C /tmp &&\  
cd /tmp && \  
opam install jupyter && \  
opam install jupyter-archimedes && \  
jupyter kernelspec install --name ocaml-jupyter "$(opam config var
share)/jupyter"  
  
# Install Go kernel  
RUN go get -u github.com/gopherdata/gophernotes && \  
mkdir -p ~/.local/share/jupyter/kernels/gophernotes && \  
cp ${GOPATH}/src/github.com/gopherdata/gophernotes/kernel/*
~/.local/share/jupyter/kernels/gophernotes  
  
ENV PATH ${PATH}:${GOPATH}/bin  
  
EXPOSE 8888  

