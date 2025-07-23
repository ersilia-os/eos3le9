FROM bentoml/model-server:0.11.0-py312
MAINTAINER ersilia

RUN pip install lazyqsar==1.0
RUN pip install numpy==1.26.4
RUN pip install rdkit==2023.9.5
RUN pip install chemprop==2.2.0

WORKDIR /repo
COPY . /repo
