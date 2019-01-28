FROM wallaroo-labs-docker-wallaroolabs.bintray.io/release/wallaroo
ADD . /code
#ADD generator /code
WORKDIR /code
#CMD "-p python3"

ENV PYTHON_INTERPRETER="python3"
ENV WALLAROO_PYTHON_ARG="python3"
RUN echo "Var $PYTHON_INTERPRETER"
RUN python --version
#RUN pip install -r requirements.txt
#EXPOSE 10000-50000
#CMD "-p python3"
#ENTRYPOINT ["/bin/sh", "-c", "\"${*}\""]
#ENTRYPOINT ["-p python3"]
#CMD ["executable","param1","param2"]
