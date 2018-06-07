FROM poad/docker-jupyter-multi-kernel-base:latest  
  
LABEL Kenji Saito "ken-yo@mbr.nifty.com"  
  
# Install IHaskell  
ENV PATH $(stack path --local-install-root)/bin:$(stack path --snapshot-
install-root)/bin:$(stack path --compiler-
bin):/root/.local/bin:/usr/local/sbin:/usr/local/bin:${PATH}  
RUN cd /root/IHaskell && \  
cp ${STACK_YAML} ${STACK_YAML}.bak && \  
sed -e "s/ - \\.\/ihaskell-display\/ihaskell-widgets/# - .\/ihaskell-
display\/ihaskell-widgets/g" ${STACK_YAML}.bak > ${STACK_YAML} && \  
stack \--resolver ${HASKELL_VERSION} \--stack-yaml ${STACK_YAML} \--no-
terminal install --no-run-benchmarks --no-run-tests --no-haddock --no-test
\--fast -j 1  
  
  

