Bootstrap: docker
From: continuumio/miniconda3
%files
./* ./

%post
# install packages.
/opt/conda/bin/conda env create -f /enviroment.yml

%runscript
. /opt/conda/bin/activate main
exec python /src/seedcoatmap.py "$@"
